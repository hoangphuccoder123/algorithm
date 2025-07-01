
import math 
m,n=map(int,input().split())
gcd=math.gcd(m,n)
m//=gcd 
n//=gcd
print(f"Phân số tối giản: {m}/{n}")
tong=0 
if m < n < 10**4 and m>0:
    for i in range(m,n+1): 
        if i % 2 ==0:
            tong+=i 
    print(tong)
else:
    print("No")
