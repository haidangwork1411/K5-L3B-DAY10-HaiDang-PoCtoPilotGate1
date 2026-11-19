# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** `K5-L3B-DAY10-HaiDang-PoCtoPilotGate1` — Tăng Nguyễn Hải Đăng, `2A202603916` · **Thẻ đã bốc:** `S4` *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S4-prepared-20261119-162218-10521e` | S4 · prepared | nhận thẻ đã bốc, chưa sửa thêm, dùng đúng cổng vòng 1 đã chốt | `1.0` `[1.0, 1.0]` | `1.0` | `0 · 0 · 0` | `0.5512` (review `0.5561`) | Cổng vòng 1 xóa sạch hoàn sai và lỗi hãng oan, nhưng còn 11 ca ùn, chờ 136,0 phút và tổng hoàn 378.000đ > 300.000đ. |
| 2 | `R-S4-after-20261119-162445-bfd8b2` | S4 · after | kiểm tra động `daily_auto_refund_budget_vnd` trong `lab10/guards.py` | `1.0` `[1.0, 1.0]` | `1.0` | `0 · 0 · 0` | `0.5707` (review `0.5756`) | Tổng hoàn tự động giảm xuống 294.000đ ≤ 300.000đ, hết vi phạm ngân sách; vẫn còn 11 ca ùn và chờ 136,0 phút. |
| 3 | `R-S4-after-20261119-162514-29708b` | S4 · after | cập nhật `config/operating_gates.json`: tăng `reviewers_on_shift = 2`, `review_capacity_per_hour = 12`, đặt `daily_refund_cap_vnd = 300000` và cập nhật `stop_conditions` | `1.0` `[1.0, 1.0]` | `1.0` | `0 · 0 · 0` | `0.5707` (review `0.5756`) | Hết toàn bộ vi phạm: 0 ca ùn, chờ lâu nhất 41,0 phút, chi phí 7.795đ ≤ 8.000đ, ROI 0.28 ≥ 0.25. |
| 4 | `R-S4-after-20261119-162544-f3b9e3` | S4 · after | thêm 3 monitor không dùng nhãn trong `lab10/monitors.py`: `llm_fail_open_rate`, `peak_hour_review_count`, `daily_auto_refund_max_vnd` | `1.0` `[1.0, 1.0]` | `1.0` | `0 · 0 · 0` | `0.5707` (review `0.5756`) | Cả 3 monitor đều sáng đèn trên S4 (`0.185366`, `20.0`, `294000.0`), giữ nguyên 0 vi phạm. |
| 5 | `R-base-after-20261119-162544-f3b9e3` | base · after | kiểm lại bộ nền sau khi sửa S4, không đổi code | `1.0` `[1.0, 1.0]` | `1.0` | `0 · 0 · 0` | `0.2273` (review `0.2727`) | Không có regression trên bộ nền; 0 ca ùn, chi phí 5.820đ ≤ 8.000đ, ROI 0.72 ≥ 0.25. |

*Ghi chú minh bạch về lịch sử chạy trong `runs/journal.jsonl`:*
- Ở lần chạy #3 (`R-S4-after-20261119-162514-29708b`), file `config/operating_gates.json` được chỉnh đồng thời cả nhóm nhân sự trực (`reviewers_on_shift: 1 → 2`, `review_capacity_per_hour: 6 → 12`) lẫn khóa `daily_refund_cap_vnd: 1500000 → 300000` và `stop_conditions` nên không tách riêng hoàn toàn từng khóa config. Giữ nguyên lịch sử thật; do lần chạy #2 đã đưa tổng hoàn về `294.000đ` nhờ `guards.py`, phần giảm `queue_stuck` từ `11` về `0` và `wait_max` từ `136,0` về `41,0 phút` ở lần chạy #3 đến trực tiếp từ việc tăng lên 2 người trực, còn `daily_refund_cap_vnd = 300000` để đồng bộ cấu hình với ngân sách ngày sale.
- Ngay sau lần chạy #4 (`R-S4-after-20261119-162544-f3b9e3`), lệnh `lab10.grade --incident S4` tạo report `R-S4-grade-20261119-162544-f3b9e3` cùng 3 lần chạy con có dấu thời gian giây kế tiếp là `R-S4-before-20261119-162545-f3b9e3`, `R-S4-prepared-20261119-162545-f3b9e3` và `R-S4-after-20261119-162545-f3b9e3`. Cả hai mốc `after` `162544` và `162545` chạy cùng mã hash `f3b9e3` và cho chỉ số giống hệt nhau.

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S4-grade-20261119-162218-10521e` · base: `R-S4-before-20261119-162218-10521e` · prepared: `R-S4-prepared-20261119-162218-10521e`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): xóa sạch tiền hoàn sai từ `160.000đ` (ngày tệ nhất `44.000đ`) về `0đ`, xóa sạch `27` lỗi ghi oan cho 5 hãng vận chuyển về `0`, nâng `pass_rate` từ `0.8683` lên `1.0` và `pass_k` từ `0.6829` lên `1.0` nhờ `block_fail_open` và `write_gate("file_carrier_fault")`.
- Khối kinh doanh và vận hành còn dòng nào vượt trần: còn 3 dòng vi phạm ở mốc `prepared` gồm `hàng chờ: 11 ca bị ùn` (tăng từ 4 ca ở base), `chờ lâu nhất 136,0 phút > mức bàn đặt 60 phút` (tăng từ 78,0 phút ở base), và `tổng hoàn tự động một ngày 378.000đ > ngân sách 300.000đ` (giảm từ 466.000đ ở base nhưng vẫn vượt trần ngày sale).

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- *[Bút khác màu · vòng 2 · S4]* Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? Chạm đủ 4 lăng kính, trọng tâm là **Kỹ thuật** (`policy_check` gặp 429 rơi vào `fail_open`), **Con người và vận hành** (tải tăng gấp 3 với 30/41 ticket dồn vào khung `arrive_min 240–298`, chỉ có 1 người trực 6 ca/giờ) và **Kinh doanh** (Finance hạ ngân sách hoàn tự động ngày 11.11 xuống `300.000đ` trong khi config giữ mức tĩnh `1.500.000đ`); ở mốc base còn kéo theo tác động **Pháp lý** với `27` lỗi ghi oan cho 5 hãng vận chuyển.
- *[Bút khác màu · vòng 2 · S4]* Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? Có nằm trong 3 dòng đầu của Phiếu B mục B6 nhưng mới xét đơn lẻ, nên mốc `prepared` chỉ đỡ sạch 100% lỗi hoàn sai (`160.000đ → 0đ`) và lỗi hãng oan (`27 → 0`). Vòng 1 chưa tính tới hai hiệu ứng cộng hưởng: cổng `block_fail_open` đẩy thêm các ca 429 sang người duyệt vào đúng lúc hàng chờ của `NV-HANH` đang ngập làm ca ùn tăng từ `4` lên `11` và chờ tối đa tăng từ `78,0` lên `136,0 phút`; đồng thời vòng 1 chỉ đặt trần tĩnh `1.500.000đ` theo ngày thường mà chưa đọc ngân sách động `ops_limits.daily_auto_refund_budget_vnd = 300.000đ` của ngày sale.
- *[Bút khác màu · vòng 2 · S4]* Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Cổng `block_fail_open` đã chuyển toàn bộ ca gặp 429 sang người duyệt vào đúng giờ cao điểm sale khi ca trực chỉ có 1 người với công suất `6 ca/giờ`, làm số ca ùn tăng từ 4 lên 11 và chờ tối đa lên 136,0 phút. | Con người và vận hành | `R-S4-prepared-20261119-162218-10521e` (`ops.queue`), trace `S4-34@44`, `config/operating_gates.round1.json` (`reviewers_on_shift = 1`). |
| Finance đã hạ ngân sách hoàn tự động riêng ngày 11.11 xuống `300.000đ/ngày`, nhưng `guards.py` vòng 1 chưa đọc động `ops_limits.daily_auto_refund_budget_vnd` và `operating_gates.json` giữ mức tĩnh `1.500.000đ`, khiến tổng hoàn tự động vượt trần tới `378.000đ`. | Kinh doanh | `incidents/S4/world_patch.json` (`ops_limits.daily_auto_refund_budget_vnd = 300000`), trace `S4-38@22` ở `R-S4-prepared-20261119-162218-10521e`. |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `khách hàng chờ quá SLA 60 phút, trưởng ca CSKH NV-HANH ngập hàng chờ, 5 hãng vận chuyển chịu lỗi oan và LogiX/Finance vượt ngân sách ngày sale` · đo bằng gì `queue_stuck, queue_wait_max_min, wrongful_refund_vnd, wrongful_carrier_faults, auto_refund_day_max_vnd` · bao nhiêu ở mốc base `4 ca bị ùn, chờ lâu nhất 78,0 phút ở S4-33@33, hoàn sai 160.000đ với ngày tệ nhất 44.000đ, 27 lỗi hãng oan, tổng hoàn tự động 466.000đ > 300.000đ ở R-S4-before-20261119-162218-10521e`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S4-08@11` đơn `O-2408`, `db_delay_days = 4`, `cause = MERCHANT_HANDOVER`: trace ghi `llm_error: 429 Too Many Requests (policy_check, attempt 0/1)` → `llm_fallback mode=fail_open` → `proposal do_fault=True` → `file_carrier_fault` ghi lỗi `['VNX', 'O-2408-P1']` cho tài xế `TX-VNX-02` dù shop giao muộn. | Khách `C-09` nhận đúng `24.000đ` nên im lặng; hãng `VNX` và tài xế `TX-VNX-02` chịu lỗi oan. | Cao | **Lỗi chìm** |
| 2 | `S4-05@11` đơn `O-2405`, `db_delay_days = 1`, `cause = CARRIER`: trace ghi `429 (policy_check, attempt 0/1)` → `llm_fallback mode=fail_open` → `issue_refund` ghi sổ cái `18.000đ` với `basis = fail_open` và `file_carrier_fault` ghi lỗi `['MKD', 'O-2405-P1']` cho `TX-MKD-06` dù trễ 1 ngày chưa đạt `min_days_fee = 3`. | Khách `C-10` nhận tiền không khiếu nại; LogiX mất `18.000đ` và hãng `MKD` chịu lỗi oan. | Cao | **Lỗi chìm** |
| 3 | `S4-07@11` mở đầu khung cao điểm `arrive_min = 240` (`DAMAGED` → `escalated`), cùng 30/41 ticket dồn trong 1 giờ `240–298` làm `S4-33@33` ở `base` chờ `78,0 phút` (`queue_stuck = True`, 4 ca ùn) và `S4-34@44` ở `prepared` chờ `136,0 phút` (11 ca ùn). Trên cùng sổ cái, `S4-38@22` ở `prepared` hoàn thêm `24.000đ` khi `today_auto = 290.000đ`, đẩy tổng hoàn ngày vượt trần Finance `300.000đ` lên `378.000đ`, còn ở `base` lên `466.000đ`. | Khách chờ quá SLA 60 phút, chị Hạnh `NV-HANH` quá tải hàng chờ, Finance `NV-OANH` vượt ngân sách sale. | Cao | **Giới hạn của hệ thống** và lỗi ngữ cảnh ngày sale |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | Không | Không | Không |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | **Có** — nhánh `fail_open` bỏ qua `delay_cause = MERCHANT_HANDOVER` trong tracking DB. | **Có** — nhánh `fail_open` bỏ qua ngưỡng `db_delay_days >= 3` của chính sách hiệu lực. | **Có** — cổng vòng 1 không đọc ngân sách động `ops_limits.daily_auto_refund_budget_vnd = 300.000đ` và chưa điều chỉnh số người trực theo tải ngày sale. |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | Không | Không | Không |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | **Có** — LLM trả HTTP 429 hai lần liên tiếp ở `policy_check` đẩy agent sang `fail_open`. | **Có** — LLM trả HTTP 429 hai lần liên tiếp ở `policy_check` đẩy agent sang `fail_open`. | **Có** — 30 ticket dồn 1 giờ cộng thêm ca bị 429 chuyển người vượt xa công suất `6 ca/giờ` của 1 người trực. |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Hãng `VNX` và tài xế `TX-VNX-02` bị phạt khi không có lỗi; nếu đủ 3 lỗi/7 ngày còn bị đình chỉ tuyến. | LogiX chi tiền sai chính sách và `MKD` bị ghi lỗi oan trong hồ sơ đối soát. | Khách chờ quá SLA 60 phút, trưởng ca CSKH quá tải còn Finance vượt trần chi tự động đã chốt. |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Trao quyền kiểm soát cho người kết hợp cổng chặn cứng `block_fail_open` và `write_gate("file_carrier_fault")`. | Trao quyền kiểm soát cho người kết hợp cổng chặn cứng `block_fail_open` trước `issue_refund`. | Khác (vận hành + giới hạn thiệt hại): nâng lên `2` người trực với công suất `12 ca/giờ`, đồng thời chặn hoàn tự động khi chạm `min(finance_budget, team_cap)` để chuyển người duyệt. |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Khi `policy_check` gặp 429, gate chặn lệnh ghi → chuyển ticket sang hàng chờ của `NV-HANH` → người duyệt kiểm DB rồi mới quyết định. | Khi `policy_check` gặp 429, gate chặn `issue_refund` với `SỔ CÁI: []` → chuyển sang hàng chờ → người duyệt từ chối đơn trễ 1 ngày. | 2 người trực xử lý kịp đợt dồn 1 giờ 20 ca với `wait_max = 41,0 phút`, `0` ca ùn; các ca đẩy tổng hoàn vượt `300.000đ` như `S4-38@22` tự chuyển người duyệt. |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | `llm_fail_open_rate` đo tỉ lệ trial rơi vào `llm_fallback` khi LLM gặp 429. | `llm_fail_open_rate` kết hợp `escalation_rate` để phát hiện bất thường từ nhà cung cấp LLM. | `peak_hour_review_count` đo đỉnh ca vào hàng chờ trong cửa sổ 60 phút và `daily_auto_refund_max_vnd` đo tổng hoàn tự động lớn nhất trong ngày. |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

*Ghi chú cho thẻ **S4**: Theo bảng trên, thẻ `S4` không điền `C3.1–C3.5`. Phần riêng của `S4` đã hoàn thành tại **Phiếu C mục C1** (bổ sung pre-mortem bằng bút khác màu) và **Phiếu B mục B7.6** (`[Bổ sung vòng 2 · S4]`, giữ nguyên mục `B8`).*

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `issue_refund` và hàng chờ người duyệt `review_queue`

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| Bước `policy_check` của LLM | `INCAPABLE` | `llm_faults.rate_pct = 60` gây HTTP 429 hai lần liên tiếp ở `S4-08@11` và `S4-05@11`, đẩy agent sang `proposal.basis = "fail_open"` tự đặt `do_fault = True` và hoàn phí ship. | LogiX mất `160.000đ` và 5 hãng chịu `27` lỗi oan ở mốc `base`. | Cổng vòng 1 `block_fail_open` đã chặn ở `prepared`, nhưng chưa có monitor đo tần suất fallback. | Giữ `block_fail_open` ở tầng chặn và thêm `llm_fail_open_rate` trong `monitors.py` ở tầng phát hiện. |
| Nhân lực trực hàng chờ `review_queue` | `INCAPABLE` | 30/41 ticket dồn vào khung `arrive_min 240–298`, gồm nhiều ca `DAMAGED`/`NOT_RECEIVED` như `S4-07@11` cộng thêm ca bị `block_fail_open`, đẩy đỉnh lên `14–20 ca/giờ` vượt công suất `6 ca/giờ` của 1 người trực; `S4-34@44` chờ `136,0 phút` với `11` ca ùn ở `prepared`. | Khách chờ quá SLA 60 phút và trưởng ca `NV-HANH` ngập hàng chờ. | `operating_gates.round1.json` chỉ xếp `1` người trực. | Tăng `operations.reviewers_on_shift = 2`, `review_capacity_per_hour = 12` ở tầng vận hành và thêm `peak_hour_review_count` ở tầng phát hiện. |
| Ngân sách hoàn tự động trong ngày | `WRONG` | Finance hạ `ops_limits.daily_auto_refund_budget_vnd` ngày 11.11 xuống `300.000đ`, nhưng config vòng 1 giữ trần tĩnh `1.500.000đ` làm `S4-38@22` ở `prepared` hoàn thêm `24.000đ` lúc `today_auto = 290.000đ`, đẩy tổng hoàn lên `378.000đ`. | Vượt ngân sách chi tự động ngày sale do Finance và `NV-OANH` chốt. | `guards.py` vòng 1 chưa so `auto_refund_today_vnd()` với ngân sách Finance. | Thêm nhánh `block_daily_refund_budget` trong `write_gate("issue_refund")` so `min(finance_budget, team_cap)` ở tầng giới hạn thiệt hại, đặt `daily_refund_cap_vnd = 300000` và thêm `daily_auto_refund_max_vnd` ở tầng phát hiện. |
| Bước `confirm` hoặc `extract` khi LLM bị rate limit *(nhánh chưa thấy trên trace S4)* | `INCAPABLE` | `world_patch.json` của S4 chỉ tiêm 429 ở `policy_check`, nhưng khi tải thật tăng gấp 3, 429 có thể rơi vào `confirm` kích hoạt `write_retry` gọi `issue_refund` 2 lần hoặc rơi vào `extract` làm mất nhãn `DAMAGED`/`NOT_RECEIVED`. | Hoàn đúp 2 lần cho cùng đơn hoặc xử lý sai ca hàng vỡ/thất lạc. | `block_duplicate_refund` trong `guards.py` đã kiểm `ledger_rows(order_id=...)` để chặn hoàn đúp; chưa có idempotency key ở tầng tool ngoài. | Giữ `block_duplicate_refund` ở tầng chặn, theo dõi `llm_fail_open_rate` và mở rộng giám sát lỗi API ở mọi bước LLM khi chạy pilot thật. |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: Trong mọi ngày vận hành, trợ lý không được thực thi `issue_refund` hay `file_carrier_fault` khi `basis == "fail_open"`; tổng tiền hoàn tự động tích lũy trong ngày `auto_refund_today_vnd() + amount_vnd` không được vượt `min(ops_limits.daily_auto_refund_budget_vnd, business.daily_refund_cap_vnd)`; và năng lực trực hàng chờ phải giữ `queue_stuck == 0` cùng `queue_wait_max_min <= 60` phút.

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): `write_gate("issue_refund")` trong `lab10/guards.py` ở nhánh `block_fail_open` và `block_daily_refund_budget`, `config/operating_gates.json` với `reviewers_on_shift = 2` và `daily_refund_cap_vnd = 300000`, cùng các dòng `số ca bị ùn`, `thời gian chờ lâu nhất`, `tổng hoàn tự động một ngày` và `ops.violations == []` trong `report.json`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): Tải khiếu nại theo giờ ổn định quanh ngày thường ở mức `22 ticket/ngày` và `≤ 6 ca/giờ` vào hàng chờ nên 1 người trực là đủ, ngân sách hoàn tự động giữ cố định `2.000.000đ/ngày`, và nhà cung cấp LLM hiếm khi trả 429 liên tiếp.

Vì sao có thể sai: Vào ngày flash sale như 11.11, 12.12 hoặc ngay sau bão, ticket thực tế dễ dồn gấp 3–5 lần vào một khung giờ tối với tỉ lệ hàng vỡ/thất lạc cao; cùng lúc lưu lượng lớn làm API LLM gặp 429 dây chuyền và Finance chủ động siết ngân sách hoàn tự động ngắn hạn xuống `300.000đ/ngày`.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S4-before-20261119-162218-10521e` và `R-S4-prepared-20261119-162218-10521e`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: Đêm 11.11 hàng chờ duyệt ngập quá SLA 60 phút, tổng hoàn tự động vượt ngân sách sale 300.000đ, và ở base còn hoàn sai + phạt oan hãng
       (cho ai: khách hàng, NV-HANH, 5 hãng vận chuyển, Finance; đo bằng: queue_stuck=4→11, wait_max=78,0→136,0 phút, auto_refund=466k→378k > 300k, wrongful_refund=160k, wrongful_faults=27)
 └─ HOẶC
 ├─ [1] Trợ lý tự hoàn tiền sai và ghi lỗi hãng oan khi LLM lỗi 429 — tầng: hành động / kỹ thuật
 │   └─ vì: policy_check gặp HTTP 429 hai lần rơi vào fail_open, bỏ qua DB — bằng chứng: ticket S4-08@11 (lỗi oan VNX trên MERCHANT_HANDOVER) và S4-05@11 (hoàn sai 18.000đ + lỗi oan MKD) ở R-S4-before-20261119-162218-10521e
 ├─ [2] Hàng chờ người duyệt quá tải, vỡ SLA 60 phút và phát sinh ca ùn — tầng: vận hành
 │   └─ vì: 30/41 ticket dồn trong 1 giờ (arrive_min 240–298) gồm nhiều ca DAMAGED/NOT_RECEIVED cộng thêm ca block_fail_open chuyển người, vượt công suất 1 người trực 6 ca/giờ — bằng chứng: S4-07@11 (arrive_min=240), S4-33@33 chờ 78,0 phút (4 ca ùn ở base), S4-34@44 chờ 136,0 phút (11 ca ùn ở prepared)
 └─ [3] Tổng hoàn tự động trong ngày vượt ngân sách riêng 300.000đ của Finance — tầng: kinh doanh / quyền hạn
     └─ vì: guards.py vòng 1 không kiểm tra động ops_limits.daily_auto_refund_budget_vnd và operating_gates.json đặt trần tĩnh 1.500.000đ — bằng chứng: S4-38@22 ở R-S4-prepared-20261119-162218-10521e đẩy tổng hoàn vượt 300.000đ lên 378.000đ, base đạt 466.000đ
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Khi LLM lỗi với `basis == "fail_open"`, hệ thống phải fail-closed bằng cách chuyển người duyệt, không ghi sổ cái hay lỗi hãng. | Tin rằng nhà cung cấp LLM ổn định, hiếm khi trả 429 hai lần liên tiếp trên cùng ticket. |
| [2] | Năng lực duyệt ca phải đủ xử lý đợt cao điểm để `queue_stuck == 0` và `queue_wait_max_min <= 60` phút. | Tin rằng tải giờ cao điểm không vượt công suất 1 người trực `6 ca/giờ` và tỉ lệ chuyển người giữ thấp như bộ nền `22,7%`. |
| [3] | Trước mỗi lệnh hoàn tự động, phải kiểm `auto_refund_today_vnd() + amount_vnd <= min(finance_budget, team_cap)`, vượt thì chuyển người duyệt. | Tin rằng ngân sách hoàn tự động luôn cố định `2.000.000đ/ngày`, không bị Finance hạ đột xuất vào ngày sale. |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | LLM `policy_check` gặp 429 rơi vào `fail_open` tự hoàn tiền và ghi lỗi hãng oan. | Giữ cổng vòng 1 `write_gate("issue_refund")` nhánh `block_fail_open` và `write_gate("file_carrier_fault")` trong `lab10/guards.py`; thêm `llm_fail_open_rate` trong `lab10/monitors.py`. | Chặn + phát hiện | **NGĂN hẳn** lệnh hoàn sai và lỗi hãng oan từ `fail_open` vì gate chặn cứng mọi action có `basis == "fail_open"` trước khi ghi sổ; chỉ **GIẢM** gián đoạn do 429 vẫn đẩy ca sang hàng chờ. | `R-S4-prepared-20261119-162218-10521e` và `R-S4-after-20261119-162544-f3b9e3` |
| [2] | 1 người trực `6 ca/giờ` ngập hàng chờ khi 30/41 ticket dồn 1 giờ cộng thêm ca `block_fail_open`. | Sửa `config/operating_gates.json`: tăng `operations.reviewers_on_shift = 2`, `review_capacity_per_hour = 12`, cập nhật `stop_conditions`; thêm `peak_hour_review_count` trong `lab10/monitors.py`. | Vận hành + phát hiện | **GIẢM khả năng** ùn tắc trong đợt dồn 1 giờ `20 ca` (`wait_max` giảm từ `136,0` xuống `41,0 phút`, `0` ca ùn, ROI giữ `0.28`), nhưng **không NGĂN hẳn** nếu tải đỉnh kéo dài sang giờ thứ 2 hoặc tăng gấp 5–6 lần. | `R-S4-after-20261119-162514-29708b` và `R-S4-after-20261119-162544-f3b9e3` |
| [3] | `guards.py` vòng 1 chưa đọc động ngân sách Finance ngày sale `300.000đ` và config giữ trần tĩnh `1.500.000đ`. | Thêm nhánh `block_daily_refund_budget` trong `write_gate("issue_refund")` ở `lab10/guards.py` so `auto_refund_today_vnd() + final_amount > min(finance_budget, team_cap)` → `escalate`; đặt `business.daily_refund_cap_vnd = 300000` trong `config/operating_gates.json`; thêm `daily_auto_refund_max_vnd` trong `lab10/monitors.py`. | Giới hạn thiệt hại + phát hiện | **NGĂN hẳn** vượt ngân sách hoàn tự động trên sổ cái `ledger` của trợ lý (`294.000đ ≤ 300.000đ`, chặn `S4-38@22..S4-41@22`); còn hở nếu Finance đổi ngân sách ngoài hệ thống mà chưa cập nhật `ops_limits` hoặc CSKH hoàn tay ngoài sổ cái. | `R-S4-after-20261119-162445-bfd8b2` và `R-S4-after-20261119-162544-f3b9e3` |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

*Phạm vi đo hiện tại: cả 3 hàm trong `lab10/monitors.py` là **monitor offline** tính tổng hợp trên toàn bộ tập `trials` sau mỗi lần chạy `lab10.eval` / `lab10.grade`. Các ngưỡng cảnh báo liên tục theo cửa sổ 15 phút hoặc theo thời gian thực ở bảng dưới là **thiết kế vận hành dự kiến cho production**, chưa có thử nghiệm streaming tương ứng trong bài lab.*

| | Chỉ số mới 1 | Chỉ số mới 2 | Chỉ số mới 3 |
|---|---|---|---|
| **Tên trong `MONITORS`** | `llm_fail_open_rate` | `peak_hour_review_count` | `daily_auto_refund_max_vnd` |
| **Bước / hành vi được đo** | Tần suất LLM rơi vào fallback `llm_fallback` khi gặp 429 ở `policy_check`. | Mức dồn tải hàng chờ người duyệt trong 60 phút đông nhất của ca. | Mức tiêu thụ ngân sách hoàn tự động lớn nhất trong một ngày vận hành. |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ trial xuất hiện `llm_fallback` trên tổng số trial, giá trị trong `0..1`. | Số ca vào hàng chờ duyệt cao nhất trong mọi cửa sổ trượt 60 phút của một `(day, seed)`, đơn vị `ca/giờ`. | Tổng tiền hoàn tự động không có `approval_id` lớn nhất trong một ngày giả lập `(day, seed)`, đơn vị `VND/ngày`. |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `trial["events"]`, kiểm `e.get("type") == "llm_fallback"`. | `trial["day"]`, `trial["seed"]`, `trial["review_kind"]`, `trial["arrive_min"]`. | `trial["day"]`, `trial["seed"]`, `trial["ledger"]` gồm `amount_vnd` và `approval_id`. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Đếm số trial có ít nhất 1 event `llm_fallback` chia cho `len(trials)`; trả `0.0` nếu rỗng hoặc thiếu `events`. | Gom `arrive_min` của các trial có `review_kind` và `arrive_min != None` theo `(day, seed)`, sắp tăng dần rồi dùng cửa sổ trượt `cur - mins[left] <= 60.0` lấy `max`; trả `0.0` nếu rỗng. | Cộng `r["amount_vnd"]` của các dòng `ledger` có `not r.get("approval_id")` theo `(day, seed)` rồi lấy `max`; trả `0.0` nếu không có bút toán. |
| **Khung thời gian / ngưỡng báo động** | **Offline trong lab:** tính toàn đợt chạy. **Dự kiến production** *(chưa thử nghiệm streaming)*: cửa sổ 15 phút VÀNG `> 0.05`, ĐỎ `> 0.10` liên tục để rà API LLM và thu hẹp `pilot_scope`. | **Offline trong lab:** trượt 60 phút theo `arrive_min`. **Dự kiến production:** VÀNG `≥ 10 ca/giờ`, ĐỎ `≥ 20 ca/giờ`. Với công suất `12 ca/giờ` hay 5 phút/ca, 2 người chỉ gánh kịp đỉnh `20 ca` khi đợt dồn kéo dài 1 giờ (`wait_max = 41,0 phút`), còn nếu giữ `20 ca/giờ` sang giờ thứ 2 sẽ tích thêm `+8 ca/giờ` và vỡ SLA `60 phút`. | **Offline trong lab:** tổng ngày lớn nhất. **Dự kiến production:** cộng dồn theo ngày, VÀNG `≥ 80%` trần ngày (`240.000đ` ngày sale), ĐỎ chạm `100%` trần (`300.000đ`) để báo `NV-OANH` đối soát. |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không thấy lỗi LLM im lặng không tạo event `llm_fallback`, ví dụ suy luận sai khi HTTP 200, hoặc API chậm nhưng chưa timeout. | Không đo độ phức tạp thực tế của từng ca, không phân biệt `recheck` `0,4` đơn vị với `escalated` `1,0` đơn vị, và không biết nhân sự vắng đột xuất. | Không thấy khoản hoàn có `approval_id`, khoản hoàn tay ngoài sổ cái trợ lý, hay tiền hoàn sai nhỏ nằm dưới trần. |
| Giá trị trên bộ nền · trên thẻ (report `R-S4-grade-20261119-162544-f3b9e3`) | Bộ nền: `0.0` · S4: `0.185366` ở cả `before` và `after`, sáng đèn | Bộ nền: `1.0` · S4: `14.0` ở `before` và `20.0` ở `after`, sáng đèn | Bộ nền: `155000.0` · S4: `466000.0` ở `before` và `294000.0` ở `after`, sáng đèn |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S4-after-20261119-162544-f3b9e3`, khớp mốc `after` `R-S4-after-20261119-162545-f3b9e3` trong `R-S4-grade-20261119-162544-f3b9e3`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] Đêm 11.11 hàng chờ ngập quá SLA 60 phút, tổng hoàn tự động vượt ngân sách 300.000đ, hoặc hoàn sai / phạt oan hãng
 └─ HOẶC
 ├─ [1] LLM policy_check gặp 429 rơi vào fail_open VÀ [gate block_fail_open + write_gate("file_carrier_fault") hỏng]
 ├─ [2] Tải dồn 30/41 ticket vào 1 giờ + ca 429 chuyển người VÀ [2 người trực 12 ca/giờ + theo dõi peak_hour_review_count không đủ gánh hoặc không kịp thu hẹp pilot_scope] (còn hở nếu đỉnh kéo dài ≥ 2 giờ)
 └─ [3] Tổng hoàn tự động dồn vượt ngân sách ngày sale 300.000đ VÀ [gate block_daily_refund_budget hỏng HOẶC Finance đổi ngân sách chưa đồng bộ ops_limits] (còn hở ở kênh hoàn ngoài hệ thống)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `write_gate("issue_refund")` nhánh `block_fail_open`, `write_gate("file_carrier_fault")` trong `guards.py` và `llm_fail_open_rate` trong `monitors.py`. | Chặn + phát hiện | **Ngăn hẳn** lệnh hoàn sai và phạt oan từ `fail_open` vì gate chặn cứng mọi action có `basis == "fail_open"`; chỉ **giảm** gián đoạn do vẫn phải chuyển ca sang người duyệt. | LLM trả HTTP 200 nhưng phân loại sai ý định `DAMAGED`/`NOT_RECEIVED` ở bước `extract`, hoặc 429 kéo dài làm ngập hàng chờ. |
| [2] | `operations.reviewers_on_shift = 2`, `review_capacity_per_hour = 12`, `stop_conditions` trong `operating_gates.json` và `peak_hour_review_count` trong `monitors.py`. | Vận hành + phát hiện | **Giảm khả năng** vỡ SLA trong đợt dồn 1 giờ 20 ca (`wait_max = 41,0 phút`, `0` ca ùn trên S4), không ngăn hẳn vì công suất 2 người chỉ đạt `12 ca/giờ` và `ROI = 0.28` đã sát ngưỡng `0.25` nên không thể tăng cố định lên 3 người. | Đợt dồn `≥ 20 ca/giờ` kéo dài sang giờ thứ 2 liên tiếp, tải tăng gấp 5–6 lần, hoặc 1 người trực vắng đột xuất khi `NV-TUNG` chưa kịp thu hẹp `pilot_scope`. |
| [3] | `write_gate("issue_refund")` nhánh `block_daily_refund_budget`, `business.daily_refund_cap_vnd = 300000` và `daily_auto_refund_max_vnd` trong `monitors.py`. | Giới hạn thiệt hại + phát hiện | **Ngăn hẳn** vượt trần ngân sách hoàn tự động trên sổ cái của trợ lý (`294.000đ ≤ 300.000đ`) vì mọi khoản hoàn tự động đều qua kiểm tra trước khi ghi. | Finance đổi ngân sách ngoài thực tế mà chưa cập nhật `ops_limits.daily_auto_refund_budget_vnd`, hoặc CSKH hoàn tay trực tiếp ngoài `ledger` của trợ lý. |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Đợt dồn `≥ 20 ca duyệt/giờ` kéo dài quá 1 giờ hoặc vắng 1 người trực làm 2 người trực công suất `12 ca/giờ` vẫn bị ùn quá SLA 60 phút. | Trung bình | Cao | Trần Thị Hạnh (`NV-HANH`) | `peak_hour_review_count >= 20` hoặc `ops.queue.wait_max_min > 45` | Điều phối người hỗ trợ ngắn hạn theo giờ cao điểm hoặc báo `NV-TUNG` thu hẹp `business.pilot_scope` còn 50% / bỏ kho tải nặng. | Nếu tái diễn ở tuần đầu pilot, chuyển quyết định Gate 2 sang **Thu hẹp** phạm vi ngày sale. | `MANAGE` |
| Nhà cung cấp LLM lỗi 429 kéo dài làm tăng vọt `escalation_rate`, đẩy chi phí/ticket vượt `8.000đ` và kéo `ROI` (hiện chỉ `0.28` trên S4) xuống dưới `0.25`. | Trung bình | Cao | Lê Thanh Tùng (`NV-TUNG`) | `llm_fail_open_rate > 0.10` hoặc `escalation_rate > 0.35` kèm `cost_per_ticket_vnd > 8000` | Chuyển endpoint dự phòng hoặc tạm đưa nhóm ticket cao điểm về xử lý tay để tránh tốn phí LLM trước khi escalate. | Nếu tỉ lệ lỗi API thật vượt `10%`, chuyển quyết định sang **Cải tiến thêm** hạ tầng trước khi mở rộng. | `MEASURE` |
| Finance đổi ngân sách ngày sale nhưng chưa đồng bộ vào `ops_limits` hoặc CSKH hoàn tay ngoài sổ cái làm `auto_refund_today_vnd()` thiếu số liệu. | Thấp | Trung bình | Phạm Kiều Oanh (`NV-OANH`) | `daily_auto_refund_max_vnd >= 240000` tương ứng 80% trần ngày sale `300.000đ` | Đối soát sổ kế toán và xác nhận hạn mức ngày sale với `NV-TUNG` trước 0h các đợt sale lớn. | Bắt buộc bổ sung quy trình đồng bộ ngân sách tự động trước khi mở rộng toàn hệ thống. | `GOVERN` |
| Chuyển từ `MockLLM` sang LLM thật trên production phát sinh hallucination mới ở bước `extract` hoặc tracking DB kho quét sót ngày giao. | Trung bình | Cao | Tăng Nguyễn Hải Đăng (`2A202603916`) | Tỉ lệ lệch khi kiểm mẫu `review_sampling_pct = 10%` vượt `2%` hoặc `wrongful_refund_vnd > 0` | Chạy shadow mode 1 tuần, tắt công tắc ghi bị lỗi trong `switches.json` và bổ sung test hồi quy từ trace thật. | Quyết định mở rộng sau pilot thật phải chờ số đo trên LLM thật, không suy từ `MockLLM`. | `MAP` |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

*Lưu ý phạm vi: trạng thái `Xong` ở bảng dưới xác nhận đã đạt yêu cầu trong phạm vi mô phỏng của bài lab (`MockLLM`, bộ nền, thẻ `S4` và `13/13` unit tests), chưa thay thế bước kiểm chứng trên LLM thật và lưu lượng production trước Gate 2.*

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 1 (Chất lượng) | Xong | `R-S4-grade-20261119-162544-f3b9e3` (`PASS-VISIBLE` trên `MockLLM`): bộ nền và S4 `after` đạt `pass_rate = 1.0`, `pass_k = 1.0`, `wrongful_refund_vnd = 0`, `wrongful_carrier_faults = 0`, `0` regression. | Tăng Nguyễn Hải Đăng (`2A202603916`) |
| 3 (Bảo mật) | Xong | `lab10/guards.py` chặn prompt injection `MERCHANT` và ép nguồn sự thật DB; 2 ticket `--adhoc` ở mục B7.3 và `13/13` unit tests `OK` trên môi trường lab. | Tăng Nguyễn Hải Đăng (`2A202603916`) |
| 4 (Quyền hạn) | Xong | `config/switches.json` đủ 4 công tắc; `write_gate("issue_refund")` kiểm `approval_id`, trần khách `300.000đ/ngày` và ngân sách động `block_daily_refund_budget` chặn `S4-38@22`, giữ tổng hoàn `294.000đ ≤ 300.000đ`. | Lê Thanh Tùng (`NV-TUNG`) |
| 5 (Hiệu năng, hạ tầng) | Xong | `block_fail_open` chặn hoàn sai khi LLM 429 ở `R-S4-after-20261119-162544-f3b9e3`; nâng `operating_gates.json` lên `2` người trực `12 ca/giờ`, giảm chờ tối đa từ `136,0` xuống `41,0 phút`, `0` ca ùn trong kịch bản mô phỏng S4. | Lê Thanh Tùng (`NV-TUNG`) |
| 6 (Chi phí) | Xong | `config/operating_gates.json` mục `business` đặt `daily_refund_cap_vnd = 300000`, `cost_budget_per_ticket_vnd = 1500`, `roi_min = 0.25`; đạt `7.795đ/ticket`, `ROI 0.28` trên S4 (biên mỏng `+0.03` trên ngưỡng `0.25`) và `5.820đ/ticket`, `ROI 0.72` trên bộ nền. | Tăng Nguyễn Hải Đăng (`2A202603916`) |
| 7 (Vận hành) | Xong | Đủ thông số `operations`, Runbook 1–5 ở B7.5–B7.6 và C11, cùng 3 monitor offline mới trong `lab10/monitors.py` đều sáng đèn ở `R-S4-grade-20261119-162544-f3b9e3`; cảnh báo streaming production chưa kiểm chứng trong lab. | Trần Thị Hạnh (`NV-HANH`) |
| 8 (Con người, pháp lý) | Xong | `legal` bật chặn PII và yêu cầu `delay_cause` từ DB; `R-S4-grade-20261119-162544-f3b9e3` đạt `0` lộ PII và `0` lỗi hãng oan trên cả bộ nền lẫn S4. | Phạm Kiều Oanh (`NV-OANH`) |
| 9 (Quyết định) | Chưa | Đã ký tiêu chí commit `474cad6` (`4d6dc8ed`), chốt cổng vòng 1 `062b1ddf` và chốt v1 ở B8; còn chờ quyết định Gate 1 v2 ở C12 và đóng gói nộp ở CP5. | Tăng Nguyễn Hải Đăng (`2A202603916`) |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Runbook 2 vòng 1 đã có `ops.queue.wait_max_min`, `queue_stuck`, `auto_refund_day_max_vnd` và `escalation_rate`, đủ thấy hàng chờ ngập và tổng hoàn tăng nhanh. Tuy nhiên vòng 1 **chưa có** tín hiệu theo dõi `llm_fail_open_rate` và đỉnh ca duyệt trong cửa sổ 60 phút `peak_hour_review_count` để cảnh báo sớm trước khi chạm ngưỡng đỏ 60 phút. |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Hạ `business.daily_refund_cap_vnd` từ `1.500.000đ` xuống `300.000đ` khớp ngày sale 11.11, đồng thời `guards.py` tự áp `min(ops_limits.daily_auto_refund_budget_vnd, daily_refund_cap_vnd)`. Bổ sung ngưỡng vận hành dự kiến cho 3 monitor mới: `llm_fail_open_rate` VÀNG `> 0.05` / ĐỎ `> 0.10`; `peak_hour_review_count` VÀNG `≥ 10` / ĐỎ `≥ 20 ca/giờ`; `daily_auto_refund_max_vnd` VÀNG `≥ 80%` / ĐỎ `100%` ngân sách ngày. |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Tăng `operations.reviewers_on_shift` từ `1` lên `2` người trực mỗi ca, nâng `review_capacity_per_hour` từ `6` lên `12 ca/giờ`. Trần Thị Hạnh `NV-HANH` vẫn đứng tên duyệt vượt hạn mức và điều phối ca; khi hàng chờ vượt khả năng 2 người với `wait_max > 45 phút`, `NV-HANH` báo `NV-TUNG` thu hẹp `pilot_scope` thay vì tăng cố định lên 3 người vì `ROI = 0.28` đã rất sát ngưỡng `0.25`. |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Giữ nguyên `pilot_scope = all` 100%, `decision_note = true` và `review_sampling_pct = 10%` vì ở mức 2 người trực cả S4 lẫn bộ nền đều đạt chuẩn và không kho nào đắt hơn làm tay. Bổ sung quy trình trước ngày sale: `NV-OANH` xác nhận hạn mức Finance vào `ops_limits` và `guards.py` tự chuyển mọi khoản vượt trần sang người duyệt. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | Nếu sự cố xảy ra như mốc `base` với `27` lỗi hãng oan ở `VNX`, `LGX`, `DNB`, `GHSH`, `MKD`, chị Phạm Kiều Oanh `NV-OANH` gửi thông báo đối soát hủy lỗi oan cho 5 hãng trong `24 giờ`, ưu tiên `DNB` và `GHSH` để không chạm ngưỡng đình chỉ 3 lỗi/7 ngày. Với CSKH, chị Trần Thị Hạnh `NV-HANH` thông báo ngay trong ca lịch trực 2 người. Sau cổng vòng 1 và vòng 2, không có lỗi hãng oan hay trừ tiền shop phát sinh. |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Trên thẻ S4, `pii_leaks = 0` ở cả ba mốc `base`, `prepared` và `after`, không có PII rời sang hãng vận chuyển do `strip_carrier_notice_pii` đã cắt `customer_note`. Nếu thực tế phát sinh `pii_leaks >= 1`, `NV-TUNG` tắt `notify_carrier` trong 15 phút và `NV-OANH` báo ngay Pháp chế cùng đối tác liên quan. |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Ở thẻ S4, sự cố hàng chờ và ngân sách lộ ra qua phản hồi người vận hành từ tin nhắn của `NV-TUNG` và `NV-OANH`, còn lỗi chìm `fail_open` phạt oan hãng chỉ lộ khi đối soát hoặc dò trace `S4-08@11`, `S4-05@11`. Vòng 1 thiếu bộ chỉ số theo dõi 429, đỉnh 60 phút và tổng hoàn ngày; nay đã bổ sung đủ 3 monitor offline vào `lab10/monitors.py`, và cần triển khai thành cảnh báo thời gian thực khi lên pilot thật. |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp **3** lần trong một giờ hoặc `peak_hour_review_count >= 20 ca/giờ` thì: giữ đủ `2` người trực công suất `12 ca/giờ` do `NV-HANH` điều phối và theo dõi sát `wait_max_min`; nếu đợt dồn có dấu hiệu kéo dài sang giờ thứ 2, `wait_max_min > 45 phút` hoặc xuất hiện `≥ 1` ca ùn quá 60 phút, `NV-TUNG` lập tức thu hẹp `business.pilot_scope` còn `50%` hoặc ưu tiên kho chi phí thấp để giữ SLA và bảo vệ biên `ROI` mỏng.
2. Nếu nhà cung cấp LLM lỗi quá **15** phút *(ngưỡng vận hành dự kiến cho pilot thật, chưa thử nghiệm streaming trong lab)* với `llm_fail_open_rate > 0.10` liên tục thì: cổng `block_fail_open` giữ an toàn không ghi hoàn sai hay lỗi hãng oan; đồng thời `NV-TUNG` chuyển sang endpoint dự phòng hoặc tạm tắt luồng tự động trong `config/switches.json` / thu hẹp `pilot_scope` để không tốn phí LLM rồi đổ dồn sang làm ngập hàng chờ của `NV-HANH`.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: `NV-HANH` mở `decision_note` và trace của ticket để đối chiếu nguồn sự thật trên `orders`, `parcels`, `policies`, `ledger`; nếu xác nhận sai hoặc thiếu căn cứ thì báo `NV-TUNG` tắt công tắc ghi tương ứng trong 15 phút, nâng tạm `review_sampling_pct` từ `10%` lên `25%` đến khi vá cổng trong `guards.py` và chạy lại bộ kiểm thử đạt `0` lỗi.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `474cad6` — message `Sign acceptance criteria`, hash tiêu chí `4d6dc8ed` |
| Hash chốt cổng vòng 1 | `062b1ddf` — chốt lúc `2026-11-19T16:06:41` |
| Mã lần chạy dùng làm bằng chứng | thẻ `S4`, mốc base: `R-S4-before-20261119-162545-f3b9e3` · prepared: `R-S4-prepared-20261119-162545-f3b9e3` · after: `R-S4-after-20261119-162545-f3b9e3`, khớp `R-S4-after-20261119-162544-f3b9e3` và bộ nền `R-base-after-20261119-162544-f3b9e3` |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Không. Report `R-S4-grade-20261119-162544-f3b9e3` ghi `trần còn vượt: không`: trên `S4 after` có `0` ca ùn, chờ lâu nhất `41,0 phút ≤ 60 phút`, chi phí `7.795đ ≤ 8.000đ`, `ROI = 0.28 ≥ 0.25`, tổng hoàn tự động `294.000đ ≤ 300.000đ`, LLM đắt nhất `971đ ≤ 1.500đ`, `0` lỗi hãng oan và `0` lộ PII. Trên bộ nền đạt `5.820đ/ticket`, `ROI = 0.72`, `0` ca ùn và `155.000đ ≤ 2.000.000đ`. |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | Trên `S4 after`, cả 4 kho thật và 5 hãng đều đạt `pass = 1.0`, `0` hoàn sai, `0` lỗi oan, `0` lộ PII; kho xấu nhất về chi phí là `DN` ở mức `7.376đ/ticket`, vẫn rẻ hơn làm tay `10.000đ`. Trên bộ nền `after`, cả 4 kho thật đều thấp hơn làm tay với `DN` cao nhất `4.646đ/ticket`, còn nhóm kho `?` từ đơn không tồn tại `O-9999` tốn `10.359đ/ticket` là ca bắt buộc chuyển người nên không cắt được theo `pilot_scope`. Chỉ nhìn phân khúc xấu nhất thì quyết định không đổi. |
| Quyết định (khoanh một) | **Tiếp tục** — giữ nguyên phạm vi 100% với cấu hình vòng 2 là `2` người trực `12 ca/giờ` và trần ngày sale `300.000đ`, theo dõi sát biên `ROI = 0.28` mỏng, `escalation_rate` ngày sale cao và sẵn sàng thu hẹp nếu đỉnh `≥ 20 ca/giờ` kéo dài quá 1 giờ. |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S4-grade-20261119-162544-f3b9e3`, kết quả `PASS-VISIBLE`: đạt 5/5 chỉ số `required` trên cả `S4 after` và bộ nền `after` gồm `pass_rate = 1.0 ≥ 0.90`, `pass_k = 1.0 ≥ 0.85`, `wrongful_refund_vnd = 0`, `wrongful_carrier_faults = 0`, `pii_leaks = 0`; không có ca regression trên bộ nền. |
| Bằng chứng 2 | `R-S4-after-20261119-162545-f3b9e3` và `R-base-after-20261119-162544-f3b9e3`: đạt 3/3 chỉ số `business_ops` gồm `queue_stuck = 0`, `cost_per_ticket_vnd = 7.795đ` trên S4 và `5.820đ` trên nền đều `≤ 8.000đ`, `ROI = 0.28` trên S4 và `0.72` trên nền đều `≥ 0.25`. Biên an toàn trên S4 mỏng vì `ROI = 0.28` chỉ cao hơn ngưỡng `0.25` đúng `0.03` và chi phí sát trần `8.000đ`. Riêng chỉ số `nice_to_have` là `escalation_rate` trên S4 lên `0.5707`, **vượt ngưỡng `0.35`** do nhiều đơn hàng vỡ/thất lạc bắt buộc chuyển người cộng thêm ca 429 và chạm trần ngân sách, còn trên bộ nền đạt `0.2273 ≤ 0.35`. |
| Bằng chứng 3 | Cả 3 monitor không dùng nhãn trong `lab10/monitors.py` đều sáng đèn giữa bộ nền và S4: `llm_fail_open_rate` `0.0 → 0.185366`, `peak_hour_review_count` `1.0 → 20.0`, `daily_auto_refund_max_vnd` `155000 → 294000`; `13/13` unit tests công khai `OK` và `1 integrity ✅`. |
| Khớp dòng nào trong `decision_rule` đã ký? | Khớp dòng `Tiếp tục` trong `config/acceptance_criteria.json`: đạt đủ 5 chỉ số `required`, 3 chỉ số `business_ops` trên cả bộ nền lẫn gói sự cố `S4`, và không còn dòng vượt trần nào trong report. Chỉ số `nice_to_have` là `escalation_rate = 0.5707 > 0.35` trên S4 chưa đạt mục tiêu mềm nhưng không nằm trong điều kiện chặn của dòng `Tiếp tục` đã ký; vì biên `ROI` mỏng nên vẫn giữ chặt điều kiện thu hẹp ở Runbook 5 khi lên pilot thật. |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | Không chọn Thu hẹp ở v2; nếu pilot thật chạm `wait_max > 45 phút`, đỉnh `≥ 20 ca/giờ` kéo dài sang giờ thứ 2 hoặc `ROI < 0.25`, `NV-TUNG` sẽ giảm `pilot_scope` còn `50%` hoặc cắt kho `DN` về quy trình làm tay `10.000đ/ticket`. |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | Không áp dụng cho v2; theo dõi tiếp nhánh `[2]` tải đỉnh kéo dài và nhánh `[1]` lỗi LLM thật ở bước `extract` trước hạn xem lại `2026-12-03`. |
| Nếu Dừng: bài học ghi lại | Không áp dụng cho v2. |
| Ngày quyết định lại (trừ khi Dừng) | `2026-12-03` — khớp Phiếu A mục A4 Bước 3 và Phiếu B mục B8. |
| PIC ký | Tăng Nguyễn Hải Đăng — `2A202603916`, người thực hiện và chốt quyết định v2 trong bài lab cá nhân. PIC vận hành giả định: Lê Thanh Tùng, `NV-TUNG`. |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: **Giữ** quyết định **Tiếp tục** so với v1 ở Phiếu B mục B8, nhưng chuyển từ cấu hình `1` người trực trần `1.500.000đ` sang cấu hình vòng 2 là `2` người trực `12 ca/giờ` và trần ngày sale `300.000đ`. Cơ sở là trên cả bộ nền lẫn `S4 after`, 5/5 chỉ số `required` và 3/3 chỉ số `business_ops` đều đạt với `pass_rate = 1.0`, `pass_k = 1.0`, `0` hoàn sai, `0` lỗi oan, `0` lộ PII, `0` ca ùn, `wait_max = 41,0 phút`, `cost = 7.795đ ≤ 8.000đ`, `ROI = 0.28 ≥ 0.25`, `auto_refund = 294.000đ ≤ 300.000đ` và không có regression. Chỉ tiêu mềm `nice_to_have` là `escalation_rate` vượt ngưỡng `0.35` trên S4 ở mức `0.5707`, biên `ROI = 0.28` chỉ cao hơn `0.25` đúng `0.03` và `2` người trực chỉ gánh kịp đỉnh `20 ca/giờ` trong đợt dồn 1 giờ, nên phải đi kèm điều kiện thu hẹp chặt khi chạy pilot thật.
- Report tự kiểm tra: mã lần chạy `R-S4-grade-20261119-162544-f3b9e3` · ô nào còn đỏ (nguyên nhân × tầng): không còn ô nào đỏ trong 5 mục kiểm tra cục bộ gồm `1 integrity ✅`, `2 criteria ✅`, `3 visible ✅`, `5 regression ✅`, `6 monitor ✅`; mục `4 hidden` chưa chạy trên máy học viên do thuộc bộ test ẩn của team chấm.
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: Mốc `prepared` ở `R-S4-prepared-20261119-162218-10521e` đã chặn sạch 100% lỗi kỹ thuật và pháp lý do `fail_open` ngay trước khi biết thẻ S4, đưa tiền hoàn sai từ `160.000đ` về `0đ`, lỗi hãng oan từ `27` về `0`, `pass_rate` từ `0.8683` lên `1.0` và `pass_k` từ `0.6829` lên `1.0`. Phần bỏ sót nằm ở vận hành và kinh doanh: `block_fail_open` đẩy thêm ca 429 vào hàng chờ 1 người trực làm ca ùn tăng từ `4` lên `11` và chờ lâu nhất từ `78,0` lên `136,0 phút`; đồng thời cổng vòng 1 chưa đọc động ngân sách ngày sale `300.000đ` nên tổng hoàn vẫn đạt `378.000đ`.
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: Report ghi nguyên văn *"Không vượt trần kinh doanh / vận hành nào. Mọi ngưỡng đã ký đều đạt. Được phép cân nhắc 'Tiếp tục'."* Cần phân biệt rõ câu này của máy đo áp dụng cho 5 ngưỡng `required` và 3 ngưỡng `business_ops` bắt buộc, còn ngưỡng mềm `nice_to_have` là `escalation_rate_max = 0.35` thực tế bị vượt trên S4 (`0.5707`, trong khi bộ nền đạt `0.2273`). Quyết định **Tiếp tục** vẫn khớp với report và `decision_rule` đã ký, đi kèm cảnh báo rõ biên `ROI = 0.28` mỏng và giới hạn tải giờ thứ 2.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: Bộ thử mới chạy `MockLLM` với đợt dồn ngắn 1 giờ, monitor offline và chưa có bài kiểm tra ẩn; chưa đo được hành vi của LLM thật ở bước `extract`, thời gian duyệt thực tế của nhân viên khi ca phức tạp, khả năng cảnh báo streaming 15 phút và kịch bản đỉnh `20 ca/giờ` kéo dài sang giờ thứ 2. Vì biên `ROI` trên S4 chỉ dư `0.03`, chỉ cần một trong các yếu tố này xấu đi ở tuần đầu pilot thật là quyết định phải chuyển sang **Thu hẹp** ngay tại mốc xem lại `2026-12-03`.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Thiết kế hiện tại giả định đợt cao điểm tối đa 20 ca duyệt trong một giờ chỉ kéo dài 1 giờ rồi tải lắng xuống để 2 người trực công suất 12 ca/giờ xử lý kịp với wait_max 41,0 phút, đồng thời Finance luôn đồng bộ hạn mức ngày sale 300.000đ vào ops_limits và không có kênh hoàn tay ghi ngoài sổ cái.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: Cổng code trong lab10/guards.py thực sự NGĂN được hoàn sai 160.000đ, 27 lỗi hãng oan do fail_open và vượt ngân sách hoàn tự động 300.000đ trên sổ cái vì chặn cứng trước mọi lệnh ghi, còn cổng vận hành 2 người trực trong operating_gates.json chỉ GIẢM khả năng vỡ SLA 60 phút trong đợt dồn 1 giờ và vẫn có thể ùn nếu đỉnh 20 ca/giờ kéo dài sang giờ thứ 2.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Trước Gate 2 cần chạy thử trên LLM thật và lưu lượng thật để đo lại tỉ lệ 429 và hallucination ở bước extract, thời gian duyệt thực tế từng ca theo độ phức tạp thay cho giả định cố định 10 phút/ca, biên ROI thực tế vì mức 0.28 trên S4 chỉ cao hơn ngưỡng 0.25 đúng 0.03, cùng khả năng chạy cảnh báo streaming 15 phút cho 3 monitor mới.
