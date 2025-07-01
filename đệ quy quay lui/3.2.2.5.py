a, b = map(int, input().split())
c = list(map(int, input().split()))
d = list(map(int, input().split()))

e = 0
f = []

def g(h, i, j, k):
    global e, f
    if i > b:
        return
    if j > e:
        e = j
        f = k[:]
    for l in range(h, a):
        g(l + 1, i + c[l], j + d[l], k + [l])
g(0, 0, 0, [])
print(e)
print("Danh sách đồ dùng được chọn:")
for m in f:
    print(f"Đồ dùng {m + 1} với giá {c[m]} và độ yêu thích {d[m]}")