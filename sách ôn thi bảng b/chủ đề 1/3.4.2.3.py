import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
prefix=[0]*(n+1)
for i in range(1,n+1):
    prefix[i]=prefix[i-1]+a[i]

for i in range(n):
    for j in range(i+1,n+1):
        if prefix 