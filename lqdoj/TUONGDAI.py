import sys 
input=sys.stdin.readline
n,k=map(int,input().split())
w=[0]+list(map(int,input().split()))
ans=0
# cài đặt prefix sum 
prefix=[0]*(n+1)
for i in range(1,n+1):
    prefix[i]=prefix[i-1]+w[i]
for _ in range(k):
    u,v=map(int,input().split())
    ans=prefix[v]-prefix[u-1]
    print(ans)