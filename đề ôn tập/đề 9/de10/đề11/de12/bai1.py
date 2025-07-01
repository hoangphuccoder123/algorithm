def uoc_chung_lon_nhat(a, b):
    if b == 0:
        return a
    return uoc_chung_lon_nhat(b, a % b)

def boi_chung_nho_nhat(a, b):
    return a * b // uoc_chung_lon_nhat(a, b)

def phan_so_toi_gian(a, b):
    gcd = uoc_chung_lon_nhat(a, b)
    return [a // gcd, b // gcd]

def so_k_tu(a, b):
    lcm = boi_chung_nho_nhat(a, b)
    k = (lcm - a % b) % b
    while (k + a) % b != 0:
        k += b
    return k

# Nhập giá trị a và b từ bàn phím
a, b = map(int, input("Nhap hai so a va b: ").split())

# In kết quả
print("Uoc chung lon nhat cua a va b:", uoc_chung_lon_nhat(a, b))
print("Boi chung nho nhat cua a va b:", boi_chung_nho_nhat(a, b))
tu, mau = phan_so_toi_gian(a, b)
print(f"Phan so toi gian cua {a}/{b}: {tu}/{mau}")
print("So k nho nhat de thoa man dieu kien:", so_k_tu(a, b))