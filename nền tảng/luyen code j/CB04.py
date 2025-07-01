a, b = map(int, input().split())

# Tính tổng
tong = a + b
print(tong)

# Tính hiệu
hieu = a - b
print(hieu)

# Tính tích
tich = a * b
print(tich)

# Tính thương
if b == 0:
    print("ERROR")
else:
    thuong = a / b
    # Làm tròn tới 2 chữ số thập phân
    thuong_format = "{:.2f}".format(thuong)
    print(thuong_format)