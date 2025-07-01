def tong_binh_phuong(x):
    t = 0
    while x:
        d = x % 10
        t += d * d
        x //= 10
    return t

def so_hanh_phuc(x):
    s = set()
    while x != 1 and x not in s:
        s.add(x)
        x = tong_binh_phuong(x)
    return x == 1

d = input()
a = int(d)

if so_hanh_phuc(a):
    print(f"{d} là số hạnh phúc!")
else:
    print(f"{d} không phải là số hạnh phúc.")

b = a
i = 1
while b != 1 and i <= 10:
    print(f"{b} -> {tong_binh_phuong(b)}")
    b = tong_binh_phuong(b)
    i += 1