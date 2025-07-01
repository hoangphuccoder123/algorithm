n = int(input())
n3=n
s1 = 0
temp = 0
while n >= 10:
    s = 1
    while n > 0:
        s *= n % 10
        n //= 10
    n = s
    s1 += 1
print(s1)

max_doben = -1
result = -1
for i in range(n3 - 1, 0, -1):
    s1 = 0
    temp = i
    while temp >= 10:
        s = 1
        while temp > 0:
            s *= temp % 10
            temp //= 10
        temp = s
        s1 += 1
    if s1 > max_doben:
        max_doben = s1
        result =  i 
print(result) 