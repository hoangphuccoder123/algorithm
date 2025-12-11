n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
tong=0
dem=0
for i in range(n):
    tong+=a[i]
    dem+=1
    if tong > 0 : 
        print(dem)
        break
    else:
        print(-1)