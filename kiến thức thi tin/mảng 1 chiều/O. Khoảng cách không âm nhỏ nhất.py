n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=a[1]-a[0]
for i in range(1,n-1):
    s=a[i+1]-a[i]
    if s<ans:
        ans=s
print(ans)
