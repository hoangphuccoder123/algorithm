# Nhập số từ bàn phím
s = input().strip()

# 1. Xóa các chữ số trùng lặp, chỉ giữ lại lần đầu tiên
da_thay = set()
s2 = ""  # Chuỗi chứa số sau khi loại bỏ chữ số trùng

for i in s:
    if i not in da_thay:
        da_thay.add(i)
        s2 += i

# 2. Chuyển dãy chữ số s2 thành danh sách số nguyên
ds = [int(i) for i in s2]

# 3. Tìm các bộ ba (a, b, c) thỏa mãn:
#    - a, b, c là 3 chữ số khác nhau
#    - a = b + c
bo_ba_so = []
for a in ds:
    for b in ds:
        for c in ds:
            if a != b and b != c and a != c:
                if a == b + c:
                    bo_ba_so.append(f"{a}{b}{c}")

# 4. In kết quả
print("So N sau khi xoa la:", s2)

if not bo_ba_so:
    print("KHONG CO")
else:
    # Nếu muốn sắp xếp giảm dần (như ví dụ), dùng lệnh dưới:
    bo_ba_so = sorted(bo_ba_so, key=lambda x: int(x), reverse=True)
    print("Bo ba so can tim la:", "; ".join(bo_ba_so))
