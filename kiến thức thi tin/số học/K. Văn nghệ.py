import math 
n,m=map(int,input().split())
so_to=math.gcd(n,m)
nam=n//so_to
nu=m//so_to
print(so_to)
print(nam,nu)