n=int(input())
a=list(map(int,input().split()))
res=0
cnt=1 
for i in range(1,n):
    if a[i] * a[i-1]<0:
        cnt+=1 
    else:
        cnt=1
res=max(res,cnt)
if res==1:
    print(1)
else:
    print(res)