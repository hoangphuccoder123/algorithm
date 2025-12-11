# --- TEMPLATE 2: MẢNG HIỆU (CẬP NHẬT ĐOẠN) ---

# 1. Nhập n (số phần tử) và q (số lần cập nhật)
n, q = map(int, input().split())

# Nhập mảng a ban đầu (nếu đề cho mảng ban đầu toàn 0 thì bỏ qua dòng này)
a = list(map(int, input().split())) 

# 2. Tạo mảng hiệu D (Lớn hơn n để tránh lỗi biên R+1)
# Ban đầu D toàn số 0
D = [0] * (n + 2)

# Nếu có mảng a ban đầu, ta khởi tạo D dựa trên a
# D[i] = a[i] - a[i-1] (Nhưng thường đề cho mảng 0 nên bước này hay bỏ qua)
# Ở đây ta giả sử mảng ban đầu là 0 cho đơn giản.

# 3. Xử lý các lượt cập nhật
for _ in range(q):
    # Đọc L, R và giá trị k cần cộng thêm
    L, R, k = map(int, input().split())
    
    # CÔNG THỨC MẢNG HIỆU:
    # Tăng đầu đoạn L lên k
    D[L] += k
    # Giảm sau cuối đoạn (R+1) đi k
    D[R+1] -= k

# 4. Cộng dồn để khôi phục mảng kết quả
ket_qua = []
val_hien_tai = 0

# Cộng dồn mảng D sẽ ra mảng giá trị thật
# Nếu có mảng a gốc, cộng thêm a[i-1] vào val_hien_tai
for i in range(1, n + 1):
    val_hien_tai += D[i]
    # Nếu bài toán yêu cầu cộng vào mảng a có sẵn thì dùng dòng dưới:
    # print(a[i-1] + val_hien_tai, end=' ') 
    print(val_hien_tai, end=' ')