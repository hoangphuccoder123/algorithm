import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
# cài đặt prefix sum 
prefix=[0]*(n+1)
for i in range(1,n+1):
    prefix[i]=prefix[i-1]+a[i-1]