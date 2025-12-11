# đọc n, k
n, k = map(int, input().split())

# đọc n dòng tiếp theo
w = [int(input()) for _ in range(n)]

# prefix sum
pre = [0] * (n + 1)
for i in range(1, n + 1):
    pre[i] = pre[i - 1] + w[i - 1]

# vì wi >= 1 nên tổng tốt nhất >= tổng k viên đầu
ans = pre[k] - pre[0]

for i in range(k, n + 1):
    cur = pre[i] - pre[i - k]
    if cur > ans:
        ans = cur

print(ans)
 