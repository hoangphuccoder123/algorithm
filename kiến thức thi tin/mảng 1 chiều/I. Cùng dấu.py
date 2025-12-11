n=int(input())
a=list(map(int,input().split()))
found=False
for i in range(n+1):
    if ((a[i]>0 and a[i+1]>0)or(a[i]<0 and a[i+1]<0)):
        print(a[i],a[i+1])
        found=True 
        break 
