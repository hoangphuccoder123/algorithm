import sys

# I/O nhanh
input = sys.stdin.readline

def sang_nto(n):
    # snt[i] = True nếu i là số nguyên tố
    snt = [True] * (n + 1)
    snt[0] = snt[1] = False

    i = 2
    # tính sẵn căn bậc 2 để không phải i * i mỗi lần
    gioi_han = int(n ** 0.5)
    while i <= gioi_han:
        if snt[i]:
            start = i * i
            buoc = i
            # dùng biến local start, buoc cho vòng for nhanh hơn chút
            for j in range(start, n + 1, buoc):
                snt[j] = False
        i += 1

    return snt


t = int(input())
doan = []
max_r = 0

for _ in range(t):
    l, r = map(int, input().split())
    doan.append((l, r))
    if r > max_r:
        max_r = r

# Sàng 1 lần
mang_nto = sang_nto(max_r)

# Prefix sum: prefix[i] = số lượng số nguyên tố trong [1..i]
prefix = [0] * (max_r + 1)
dem = 0
for i in range(1, max_r + 1):
    if mang_nto[i]:
        dem += 1
    prefix[i] = dem

# Trả lời tất cả query, gom output in 1 lần
out = []
for l, r in doan:
    so_nto = prefix[r] - prefix[l - 1]
    out.append(str(so_nto))

sys.stdout.write("\n".join(out))
 