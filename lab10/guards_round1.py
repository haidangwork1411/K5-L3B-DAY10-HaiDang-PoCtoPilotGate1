"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
import re

from . import helpers as H  # noqa: F401
from .tools import Verdict

_DEFAULT_NOTICE_FIELDS = frozenset({"order_id", "parcel_id", "district", "delay_days"})
_PHONE_RE = re.compile(r"(?:\+?84|0)(?:[\s.\-]*\d){8,10}")


def _safe_policy(ctx):
    """Tra cứu chính sách đang hiệu lực tại ctx.as_of; trả về None nếu dữ liệu ngày/chính sách lỗi."""
    try:
        policies = ctx.tools.lookup_policies()
        if not isinstance(policies, list) or not policies or not ctx.as_of:
            return None
        return H.effective_policy(policies, ctx.as_of)
    except (KeyError, TypeError, ValueError):
        return None


def _safe_parcel_and_delay(order, ticket, as_of):
    """Lấy kiện hàng mục tiêu và số ngày trễ từ tracking DB; trả về (None, None) nếu thiếu/lỗi dữ liệu."""
    if not isinstance(order, dict) or not as_of:
        return None, None
    parcels = order.get("parcels")
    if not isinstance(parcels, list) or not parcels:
        return None, None
    try:
        parcel = H.ticket_parcel(order, ticket or {}, as_of)
        if not isinstance(parcel, dict) or not parcel.get("parcel_id") or not parcel.get("carrier_id"):
            return None, None
        db_delay = H.db_delay_days(parcel, as_of)
        return parcel, db_delay
    except (KeyError, TypeError, ValueError):
        return None, None


def pre_guard(ctx):
    """Cổng 1A: ghim đúng phiên bản chính sách đang hiệu lực tại ctx.as_of (chống lệch cờ index_active)."""
    pol = _safe_policy(ctx)
    if pol is not None and pol.get("policy_id"):
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def _valid_approval(ctx, approval_id, order_id, ticket_id, amount_vnd):
    """Kiểm tra mã phê duyệt tồn tại, còn hiệu lực, khớp đúng đơn/ticket, đủ hạn mức và chưa dùng trên sổ cái."""
    if not approval_id or not order_id or not ticket_id:
        return False
    cands = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not cands:
        return False
    a = cands[0]
    if a.get("status") != "valid":
        return False
    if a.get("order_id") != order_id or a.get("ticket_id") != ticket_id:
        return False
    if (a.get("expires_at") or "") < (ctx.as_of or ""):
        return False
    max_vnd = a.get("max_vnd")
    if not isinstance(max_vnd, (int, float)) or isinstance(max_vnd, bool) or max_vnd < amount_vnd:
        return False
    if ctx.tools.ledger_rows(approval_id=approval_id):
        return False
    return True


def _sanitize_notice_value(key, val, recipient):
    """Loại bỏ PII (tên, địa chỉ, SĐT người nhận hoặc chuỗi SĐT) nếu bị nhúng trong giá trị trường được phép."""
    if not isinstance(val, str):
        return val, False
    cleaned = val
    changed = False
    rc = recipient if isinstance(recipient, dict) else {}

    for field in ("name", "street"):
        token = rc.get(field)
        if isinstance(token, str) and token.strip():
            pat = re.compile(re.escape(token.strip()), re.I)
            if pat.search(cleaned):
                cleaned = pat.sub("[REDACTED]", cleaned)
                changed = True

    rc_phone = H.digits(rc.get("phone", ""))[-9:]
    if rc_phone and rc_phone in H.digits(cleaned):
        cleaned = _PHONE_RE.sub("[REDACTED]", cleaned)
        if rc_phone in H.digits(cleaned):
            cleaned = "[REDACTED]"
        changed = True

    if key not in ("order_id", "parcel_id") and _PHONE_RE.search(cleaned):
        cleaned = _PHONE_RE.sub("[REDACTED]", cleaned)
        changed = True

    return cleaned, changed


def write_gate(ctx, action):
    """Cổng phòng ngừa vòng 1 trước mỗi lệnh ghi (dựa hoàn toàn vào nguồn sự thật DB và chính sách hiệu lực)."""
    if not isinstance(action, dict):
        return Verdict.escalate("tham số lệnh ghi không hợp lệ: chuyển người duyệt")
    tool = action.get("tool")

    # Cổng 1B: Kiểm soát lệnh ghi tiền issue_refund
    if tool == "issue_refund":
        order_id = action.get("order_id")
        if action.get("basis") == "fail_open":
            ctx.log("block_fail_open", order_id=order_id)
            return Verdict.escalate("LLM lỗi 429 (fail_open): không tự hoàn tiền, chuyển người duyệt")

        if not order_id:
            ctx.log("block_missing_facts", order_id=order_id)
            return Verdict.escalate("thiếu mã đơn hàng trong lệnh hoàn: chuyển người duyệt")

        if ctx.tools.ledger_rows(order_id=order_id):
            ctx.log("block_duplicate_refund", order_id=order_id)
            return Verdict.deny("đơn đã có bút toán hoàn tiền trên sổ cái, chặn hoàn trùng")

        order = ctx.tools.lookup_order(order_id)
        pol = _safe_policy(ctx)
        parcel, db_delay = _safe_parcel_and_delay(order, ctx.ticket, ctx.as_of)
        if order is None or pol is None or parcel is None:
            ctx.log("block_missing_facts", order_id=order_id, has_order=order is not None,
                    has_policy=pol is not None, has_parcel=parcel is not None)
            return Verdict.escalate("thiếu dữ liệu đơn hàng, kiện hàng hoặc chính sách hiệu lực: chuyển người duyệt")

        cause = parcel.get("delay_cause")
        try:
            expected = H.entitlement_vnd(pol, order, db_delay, cause)
            auto_limit = pol["auto_limit_vnd"]
        except (KeyError, TypeError, ValueError):
            ctx.log("block_invalid_policy_data", order_id=order_id)
            return Verdict.escalate("dữ liệu chính sách hoặc đơn hàng không đầy đủ để tính quyền lợi: chuyển người duyệt")

        if expected <= 0:
            ctx.log("block_ineligible_refund", order_id=order_id, db_delay=db_delay,
                    cause=cause, asked=action.get("amount_vnd"))
            return Verdict.deny(f"không đủ điều kiện hoàn theo DB (trễ {db_delay} ngày, nguyên nhân {cause})")

        if action.get("payer", "LOGIX") != "LOGIX":
            ctx.log("block_non_logix_payer", order_id=order_id, payer=action.get("payer"))
            return Verdict.escalate("không cho phép tự trừ tiền bên khác (MERCHANT): chuyển người duyệt")

        changes = {}
        final_amount = action.get("amount_vnd")
        if not isinstance(final_amount, (int, float)) or isinstance(final_amount, bool) or final_amount != expected:
            ctx.log("fix_refund_amount", order_id=order_id, asked=final_amount,
                    expected=expected, db_delay=db_delay)
            changes["amount_vnd"] = expected
            final_amount = expected

        approval_id = action.get("approval_id")
        has_valid_approval = _valid_approval(ctx, approval_id, order_id, action.get("ticket_id"), final_amount)
        if approval_id and not has_valid_approval:
            ctx.log("strip_invalid_approval", order_id=order_id, approval_id=approval_id, amount_vnd=final_amount)
            changes["approval_id"] = None

        if final_amount > auto_limit:
            if not has_valid_approval:
                ctx.log("block_invalid_approval", order_id=order_id, approval_id=approval_id,
                        amount_vnd=final_amount, auto_limit_vnd=auto_limit)
                return Verdict.escalate("khoản hoàn vượt hạn mức tự động và thiếu phê duyệt hợp lệ cho đúng đơn/ticket")
        elif not has_valid_approval:
            cust_cap = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
            if cust_cap is not None:
                cust_spent = sum(
                    r["amount_vnd"] for r in ctx.tools.ledger_rows(customer_id=order.get("customer_id"))
                    if not r.get("approval_id")
                )
                if cust_spent + final_amount > cust_cap:
                    ctx.log("block_customer_daily_cap", customer_id=order.get("customer_id"),
                            spent=cust_spent, asked=final_amount, cap=cust_cap)
                    return Verdict.escalate("vượt trần hoàn tự động theo khách trong ngày: chuyển người duyệt")

        if changes:
            return Verdict.modify("điều chỉnh lệnh hoàn khớp nguồn sự thật DB và trạng thái phê duyệt", **changes)
        return Verdict.allow()

    # Cổng 2: Bảo vệ bên thứ ba khi ghi lỗi hãng file_carrier_fault
    if tool == "file_carrier_fault":
        order_id = action.get("order_id")
        if not order_id:
            ctx.log("block_carrier_fault_missing_facts", order_id=order_id)
            return Verdict.deny("thiếu mã đơn hàng để ghi lỗi hãng")

        order = ctx.tools.lookup_order(order_id)
        pol = _safe_policy(ctx)
        parcel, db_delay = _safe_parcel_and_delay(order, ctx.ticket, ctx.as_of)
        if order is None or pol is None or parcel is None:
            ctx.log("block_carrier_fault_missing_facts", order_id=order_id, has_order=order is not None,
                    has_policy=pol is not None, has_parcel=parcel is not None)
            return Verdict.deny("thiếu dữ liệu đơn hàng, kiện hàng hoặc chính sách hiệu lực để ghi lỗi hãng")

        try:
            at_fault = H.carrier_at_fault(pol, parcel, db_delay)
        except (KeyError, TypeError, ValueError):
            ctx.log("block_carrier_fault_invalid_policy", order_id=order_id)
            return Verdict.deny("dữ liệu chính sách không đầy đủ để xác định lỗi hãng")

        if not at_fault:
            ctx.log("block_invalid_carrier_fault", order_id=order_id, parcel_id=parcel["parcel_id"],
                    db_delay=db_delay, cause=parcel.get("delay_cause"))
            return Verdict.deny("không đủ căn cứ ghi lỗi hãng theo tracking DB và chính sách hiệu lực")

        target_carrier = parcel["carrier_id"]
        strike_cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        today_strikes = len(ctx.tools.fault_rows(carrier_id=target_carrier))
        if strike_cap is not None and today_strikes >= strike_cap:
            ctx.log("block_carrier_strike_cap", carrier_id=target_carrier,
                    today_strikes=today_strikes, cap=strike_cap)
            return Verdict.deny(f"hãng {target_carrier} đã đạt trần {strike_cap} lỗi tự động/ngày")

        changes = {}
        for k, v in (
            ("parcel_id", parcel["parcel_id"]),
            ("carrier_id", target_carrier),
            ("driver_id", parcel.get("driver_id")),
            ("delay_days", db_delay),
        ):
            if action.get(k) != v:
                changes[k] = v
        if changes:
            ctx.log("fix_carrier_fault_target", order_id=order_id, changes=changes)
            return Verdict.modify("sửa mục tiêu lỗi hãng khớp kiện bị trễ trong tracking DB", **changes)
        return Verdict.allow()

    # Cổng 3: Lọc dữ liệu cá nhân (PII) trước khi gửi bản tin notify_carrier
    if tool == "notify_carrier":
        pol = _safe_policy(ctx)
        fields = pol.get("carrier_notice_fields") if isinstance(pol, dict) else None
        allowed = set(fields) if isinstance(fields, list) and fields else set(_DEFAULT_NOTICE_FIELDS)

        raw_payload = action.get("payload")
        if not isinstance(raw_payload, dict):
            ctx.log("block_invalid_carrier_notice_payload", carrier_id=action.get("carrier_id"))
            return Verdict.deny("payload thông báo hãng không hợp lệ")

        order_id = raw_payload.get("order_id") or (ctx.ticket or {}).get("order_id")
        order = ctx.tools.lookup_order(order_id) if order_id else None
        recipient = order.get("recipient") if isinstance(order, dict) else None

        clean = {}
        redacted_keys = []
        for k, v in raw_payload.items():
            if k not in allowed:
                continue
            safe_v, was_redacted = _sanitize_notice_value(k, v, recipient)
            clean[k] = safe_v
            if was_redacted:
                redacted_keys.append(k)

        dropped = sorted(set(raw_payload.keys()) - set(clean.keys()))
        if dropped or redacted_keys:
            ctx.log("strip_carrier_notice_pii", carrier_id=action.get("carrier_id"),
                    dropped=dropped, redacted_keys=sorted(redacted_keys))
            return Verdict.modify("chỉ giữ trường được phép và lọc PII trong giá trị gửi hãng", payload=clean)
        return Verdict.allow()

    return Verdict.allow()
