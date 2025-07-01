a, b = map(int, input().split())
s = 0
for i in range(1, a+1):
    if a % i == 0:
        if b % i != 0:
            s += i
print(s)