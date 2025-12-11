n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
cnt=0
for i in range(n-2):
    l=i+1
    r=n-1
    while l < r :
        s=a[i] + a[l] + a[r]
        if s==k:
            cnt+=1
        elif tong<k:
            l+=1 
        else:
            r-=1 
print(cnt)
