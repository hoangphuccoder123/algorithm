n, k = map(int, input().split())
count = 0
# Calculate the range for i
for i in range(1, min(n, (k - 1) // 2) + 1):
    j = k - i
    if j > i and j <= n:
        count += 1
print(count)
