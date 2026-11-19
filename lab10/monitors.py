"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def llm_fail_open_rate(trials):
    """Tỉ lệ trial rơi vào chế độ fallback (llm_fallback) khi nhà cung cấp LLM gặp lỗi 429."""
    if not trials:
        return 0.0
    hits = sum(
        any(e.get("type") == "llm_fallback" for e in (t.get("events") or []))
        for t in trials
    )
    return hits / len(trials)


def peak_hour_review_count(trials):
    """Số ca cần người duyệt nhiều nhất trong bất kỳ cửa sổ trượt 60 phút nào của một ngày vận hành."""
    if not trials:
        return 0.0
    by_day_seed = {}
    for t in trials:
        if t.get("review_kind") and t.get("arrive_min") is not None:
            key = (t.get("day"), t.get("seed"))
            by_day_seed.setdefault(key, []).append(float(t["arrive_min"]))
    peak = 0
    for mins in by_day_seed.values():
        mins.sort()
        left = 0
        for right, cur in enumerate(mins):
            while cur - mins[left] > 60.0:
                left += 1
            if right - left + 1 > peak:
                peak = right - left + 1
    return float(peak)


def daily_auto_refund_max_vnd(trials):
    """Tổng tiền hoàn tự động (không có approval_id) lớn nhất trong một ngày vận hành giả lập."""
    if not trials:
        return 0.0
    by_day_seed = {}
    for t in trials:
        key = (t.get("day"), t.get("seed"))
        amt = sum(
            r.get("amount_vnd", 0)
            for r in (t.get("ledger") or [])
            if not r.get("approval_id")
        )
        by_day_seed[key] = by_day_seed.get(key, 0) + amt
    return float(max(by_day_seed.values(), default=0))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "llm_fail_open_rate": llm_fail_open_rate,
    "peak_hour_review_count": peak_hour_review_count,
    "daily_auto_refund_max_vnd": daily_auto_refund_max_vnd,
}
STARTER_MONITORS = ("escalation_rate",)
