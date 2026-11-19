# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `HaiDang`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-HaiDang-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S4`
- Ghi chú hình thức thực hiện: **Em xin phép bài lab được thực hiện cá nhân do không tìm được nhóm.**

## Thành viên

Họ tên đầy đủ và MSSV của thành viên thực hiện (học viên làm cá nhân, đảm nhiệm cả ba vai theo README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Tăng Nguyễn Hải Đăng | 2A202603916 | Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý | Có |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên: `["TangNguyenHaiDang-2A202603916"]`.

## Cá nhân

## TangNguyenHaiDang-2A202603916

### Phần việc phụ trách

Thực hiện cá nhân toàn bộ ba vai của Lab 10:
- **Kỹ sư cổng:** thiết lập môi trường, chạy đánh giá & trace, viết cổng phòng ngừa trong `lab10/guards.py`, thêm chỉ số theo dõi trong `lab10/monitors.py`, kiểm tra regression và test công khai.
- **Sản phẩm và kinh doanh:** xây dựng tiêu chí chấp nhận (`config/acceptance_criteria.json`), Phiếu A, cổng kinh doanh trong `config/operating_gates.json` (`business`), quyết định Gate 1 v1 (Phiếu B mục B8) và v2 (Phiếu C mục C12).
- **Vận hành và pháp lý:** HAZOP mở rộng, checklist 9 nhóm việc, cổng vận hành & pháp lý trong `config/operating_gates.json` (`operations`, `legal`), runbook phần 1–5 & giờ cao điểm, gom bài nộp trong `submission/`.

### Đóng góp cụ thể

- **CP1:**
  - Thiết lập cấu hình Git cục bộ (`user.name=2A202603916`, `user.email=2A202603916@example.com`), cấu hình remote `origin` qua SSH alias `github-study` và `upstream` trỏ tới repo đề, xác minh repo cá nhân ở chế độ Public được tạo bằng "Use this template".
  - Đọc toàn bộ đề bài, rubric, quy định, mẫu phiếu A/B/C, mã nguồn Lab 10 và đối chiếu số liệu nền từ Lab 9.
  - Hoàn thiện `TEAM.md` ban đầu và chạy bộ 13 unit tests công khai (`13/13 OK`).
- **CP2:**
  - Hoàn thiện Phiếu A (`templates/form-a-criteria.md`, mục A1–A5) và `config/acceptance_criteria.json` với 9 ngưỡng chấp nhận trước khi chạy `eval`.
  - Ký tiêu chí bằng `python3 -m lab10.criteria sign` và commit/push trước lần đánh giá đầu tiên.
- **CP3:**
  - Chạy `base`, soát lỗi `T-002@55`, lập bản đồ dữ liệu, HAZOP vòng 1, checklist 9 nhóm, pre-mortem 4 lăng kính và viết cổng phòng ngừa vòng 1 trong `lab10/guards.py` cùng `config/operating_gates.json`.
  - Chạy `python3 -m lab10.checkpoint` chốt mốc vòng 1, đánh giá `prepared` trên bộ nền và chốt quyết định Gate 1 v1 (`Tiếp tục`) ở Phiếu B (`B0–B8`).
- **CP4:**
  - Nhận duy nhất thẻ `S4` từ repo thẻ chính thức, chạy `lab10.grade --incident S4` trước khi sửa, dò trace `S4-08@11`, `S4-05@11`, `S4-07@11`, `S4-33@33`, `S4-34@44`, `S4-38@22`.
  - Bổ sung kiểm tra ngân sách động `block_daily_refund_budget` trong `lab10/guards.py`, tăng `reviewers_on_shift = 2` và đặt `daily_refund_cap_vnd = 300000` trong `config/operating_gates.json`, thêm 3 monitor không dùng nhãn trong `lab10/monitors.py`.
  - Hoàn thiện Phiếu C (`C0–C11`) và cập nhật mục Giờ cao điểm `B7.6` ở Phiếu B.
- **CP5:**
  - Hoàn thiện quyết định Gate 1 v2 (`Tiếp tục` kèm ràng buộc biên `ROI = 0.28` và giới hạn tải giờ thứ 2) và ba dòng bắt buộc ở Phiếu C mục `C12`.
  - Điền `submission/submission.json`, gom bài nộp bằng `python3 -m lab10.check_submission --collect` và kiểm tra đủ thành phần trước khi nộp.
- **Sử dụng công cụ AI (theo `RULES.md`):**
  - Có dùng AI coding agent hỗ trợ chạy lệnh đánh giá và rà soát câu chữ trong phiếu. Mọi ngưỡng tiêu chí, tham số cổng vận hành, phân tích nguyên nhân và quyết định Gate 1 v1/v2 đều được cá nhân trực tiếp rà soát, kiểm chứng trên report thật và chịu trách nhiệm giải trình.

### Bằng chứng

- **CP1:** commit `0dc656e`, `git remote -v`, `python3 -m unittest discover -s tests` (`13/13 OK`).
- **CP2:** commit `474cad6` (`Sign acceptance criteria`, hash `4d6dc8ed`), commit `bc1dd04`, `templates/form-a-criteria.md`.
- **CP3:** commit `13d7e17` (chốt vòng 1 hash `062b1ddf`), commit `a518404`, `R-base-before-20261119-153523-b45eeb`, `R-base-prepared-20261119-160653-10521e`, `templates/form-b-evaluation-gates.md`.
- **CP4:** commit `c2a8978` (`Nhận thẻ S4`), commit `7b76d4f`, `R-S4-grade-20261119-162218-10521e` (trước sửa), `R-S4-grade-20261119-162544-f3b9e3` (`PASS-VISIBLE`), `R-S4-after-20261119-162544-f3b9e3`, `R-base-after-20261119-162544-f3b9e3`.
- **CP5:** `templates/form-c-incident.md` (`C12`), `submission/submission.json`, `submission/manifest.json`, output `python3 -m lab10.check_submission --collect` (`ĐỦ THÀNH PHẦN`).

### Exit ticket

- Đưa hệ thống AI từ PoC sang Pilot không chỉ là tối ưu model mà phải khóa cứng các lệnh ghi bằng nguồn sự thật ngoài model, đặt trần ngân sách động và tính đúng công suất người trực giờ cao điểm.
- Một cổng chặn an toàn như `block_fail_open` có thể đẩy tải sang hàng chờ người duyệt nếu không tính kèm năng lực vận hành, và mức đạt `PASS` với `ROI = 0.28` sát ngưỡng `0.25` vẫn cần điều kiện thu hẹp rõ ràng khi chạy pilot thật.
