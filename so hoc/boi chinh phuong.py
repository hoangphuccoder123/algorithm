n=int(input())
Mod=int(1e9+7)
a=list(map(int,input().split()))
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)

def tim_so_chinh_phuong(num):
    i = 2 
    s = {}
    temp = num
    while i*i <= temp:
        count = 0
        while temp % i == 0:
            count += 1
            temp //= i
        if count > 0:
            s[i] = count
        i += 1
    if temp > 1:
        s[temp] = 1
    return s

s = a[0]
for i in range(1,n):
    s = lcm(s,a[i])

factors = tim_so_chinh_phuong(s)
result = 1

for prime, exp in factors.items():
    if exp % 2 == 1:
        result = (result * prime) % Mod

result = (result * result) % Mod
print(result)