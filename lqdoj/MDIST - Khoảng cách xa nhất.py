import sys 
input=sys.stdin.readline 
n=int(input())
b=list(map(int,input().split()))
b.sort()
r=list(map(int,input().split()))
r.sort()
i=0 
j=0 
max_diff=-10**18 
if len(b) and len(r)==1:
    max_diff=abs(b[0]-r[0])
for i in range(n):
    for j in range(n):
        max_diff=max(max_diff,abs(b[i]-r[j])+abs(b[j]-r[i]))
print(max_diff)