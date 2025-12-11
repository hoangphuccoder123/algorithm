n=int(input())
a=list(map(int,input().split()))
tong=0
dem=0
for i in range(n):
    if a[i]%2==1 and(i+1)%2==0:
        tong+=a[i]
        dem+=1 
if dem==0:
    print("NO")
else:
    tbc=tong/dem
    print(f"{tbc:.5f}")