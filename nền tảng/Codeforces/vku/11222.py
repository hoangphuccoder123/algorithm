n = int(input())
a = list(map(int, input().split()))
d = {}
count = 0

# Đếm số lần xuất hiện của từng số
for i in range(n):
    if a[i] in d:
        d[a[i]] += 1
    else:
        d[a[i]] = 1

# Tính toán số nhóm có thể tạo ra
for j in d:
    if d[j] < 2:
        count = -1
        break
    elif d[j] % 3 == 0:
        count += d[j] // 3
    elif d[j] % 3 == 2:
        count += d[j] // 3 + 1
    elif d[j] % 3 == 1:
        count += d[j] // 3 + 1
print(count) 