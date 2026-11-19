# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `HaiDang`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-HaiDang-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):
- Ghi chú hình thức thực hiện: **Bài lab được thực hiện cá nhân do không tìm được nhóm.**

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
  - Đọc và kiểm toán toàn bộ tài liệu hướng dẫn, đề bài, rubric, quy định, mẫu phiếu A/B/C và mã nguồn/dữ liệu của Lab 10.
  - Đối chiếu tài liệu nền từ Lab 9 (`docs/eval_card.md`, `docs/PRD_v1.1.md`, `docs/failure_taxonomy.md`, `docs/judge_audit.md`, `docs/trace_case.md` và các báo cáo JSON thực tế).
  - Hoàn thiện `TEAM.md` và chạy kiểm tra bộ 13 unit tests công khai (`python3 -m unittest discover -s tests`).

### Bằng chứng

- **CP1:** `git remote -v`, `git config --list --local`, output `python3 -m unittest discover -s tests` (13/13 PASS), chỉnh sửa `TEAM.md`.

### Exit ticket
