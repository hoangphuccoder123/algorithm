n,k=map(int,input().split())
a=list(map(int,input().split())) 
nguoi_nhan=[0]*n
for i in range(1,n):
    t1=a.pop()
    t2=a.pop()
    if t1>t2:
        nguoi_nhan[i-1]=t1 
        a.insert(0,t2)
    else: 
        nguoi_nhan[i-1]=t2
        a.insert(0,t1)
nguoi_nhan[n-1]=a[0]
for i in range(n):
    if i==k-1:
        print(nguoi_nhan[i])
        break
        