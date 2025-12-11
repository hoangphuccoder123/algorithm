n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dem_a={}
for x in a:
    if x in dem_a:
        dem_a[x]+=1 
    else:
        dem_a[x]=1 
ans =0 
for x in b:
    if x in dem_a:
        ans+=dem_a[x]
print(ans)