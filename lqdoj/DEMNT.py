import math 
import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(n):
    for j in range(i+1,n):
        if math.gcd(a[i],a[j])==1:
            cnt+=1
print(cnt)