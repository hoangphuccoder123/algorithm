n,l,r=map(int,input().split())
a=list(map(int,input().split()))
prefix=[0]*(n+1)
for i in range(1,n+1):
    prefix[i]=prefix[i-1]+a[i-1]

ans=-10**18 
for l in range(l,r+1):
    for i in range(l,n+1):
        total=prefix[i] - prefix[i-l]
        if total>ans:
            ans=total 
print(ans)