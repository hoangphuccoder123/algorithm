# --- TEMPLATE 3: MẢNG CỘNG DỒN 2 CHIỀU ---

# 1. Nhập kích thước n hàng, m cột
n, m = map(int, input().split())

# Nhập ma trận a
a = []
for _ in range(n):
    hang = list(map(int, input().split()))
    a.append(hang)

# 2. Xây dựng mảng cộng dồn 2 chiều S
# Kích thước (n+1) x (m+1) đệm số 0
S = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # CÔNG THỨC XÂY DỰNG:
        # Giá trị hiện tại + Tổng trên + Tổng trái - Tổng chéo (trùng lặp)
        val = a[i-1][j-1]
        S[i][j] = val + S[i-1][j] + S[i][j-1] - S[i-1][j-1]

# 3. Truy vấn tổng hình chữ nhật
# Giả sử cần tính tổng hcn từ (x1, y1) đến (x2, y2)
# q = int(input()) # Số câu hỏi
# for _ in range(q):
#     x1, y1, x2, y2 = map(int, input().split())
    
#     # CÔNG THỨC TÍNH TỔNG:
#     # Tổng lớn - Phần dư trên - Phần dư trái + Phần dư chéo
#     tong = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
#     print(tong) 