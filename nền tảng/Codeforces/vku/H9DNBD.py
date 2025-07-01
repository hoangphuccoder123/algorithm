n, k = map(int, input().split())
a = list(map(int, input().split()))
count = {}
s = 0
l = 0
for num in a:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for key, value in count.items():
    if value >= k:
        s += 1
        l += key 
print(s, l)
