import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    if (i+1)%2==0:
        s+=a[i]
print(s)