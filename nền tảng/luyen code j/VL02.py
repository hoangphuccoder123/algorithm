n = int(input())

if n < 0:
    print("Không tính tổng cho n âm")
else:
    # Sử dụng // thay vì / để đảm bảo kết quả là số nguyên
    s = (n + 1) * n // 2
    print(s)