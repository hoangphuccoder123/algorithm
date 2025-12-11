n,x=map(int,input().split())
a=list(map(int,input().split()))
gan=a[0]
xa=a[0]
kcach_min=abs(a[0]-x)
kach_max=abs(a[0]-x)
for i in range(1,n):
    val=a[i]
    d=abs(val-x)
# tìm số gần nhất 
    if d<kcach_min or(d==kcach_min and val<gan):
        kcach_min=d
        gan=val 
    if d>kach_max:
        kach_max=d  
        xa=val
print(gan,xa)