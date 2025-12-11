import math 
n,x,y=map(int,input().split()) 
ucln=math.gcd(x,y)
bcln=(x*y)//ucln 
cnt=n//bcln
print(cnt)