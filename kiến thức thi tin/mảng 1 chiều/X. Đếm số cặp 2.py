n,k=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
for i in range(n):
    for j in range(i+1,n):
        if a[i]+a[j]==k:
            cnt+=1 
print(cnt)