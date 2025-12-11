n,k=map(int,input().split())
a=list(map(int,input().split()))
count=0
for l in range(n):
    for r in range(l+1,n):
        if abs(a[r]-a[l])==k:
            count+=1 
print(count) 