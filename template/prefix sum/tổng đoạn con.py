# --- TEMPLATE 1: MẢNG CỘNG DỒN 1 CHIỀU ---

# 1. Nhập dữ liệu
# n là số phần tử, q là số câu hỏi (nếu có)
dong_dau = list(map(int, input().split()))
n = dong_dau[0]
# q = dong_dau[1] (nếu đề có số lượng truy vấn)

# Nhập mảng a
a = list(map(int, input().split()))

# 2. Xây dựng mảng cộng dồn S (Có thêm số 0 ở đầu)
S = [0] * (n + 1)
tong_tam = 0
for i in range(n):
    tong_tam = tong_tam + a[i]
    S[i+1] = tong_tam

# 3. Trả lời truy vấn hoặc xử lý
# Ví dụ: Tính tổng từ L đến R
# LƯU Ý: Nếu đề bài tính vị trí từ 1, giữ nguyên L, R
# Nếu đề bài tính từ 0, có thể cần chỉnh L, R tùy đề
# Template này giả sử input L, R tính từ 1

# (Phần này thay đổi tùy đề bài)
# Ví dụ: Đọc q câu hỏi L, R
# for _ in range(q):
#     L, R = map(int, input().split())
#     tong = S[R] - S[L-1]
#     print(tong)