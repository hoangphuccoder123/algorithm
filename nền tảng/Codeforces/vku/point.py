
n,t=map(int,input().split())
a=list(map(int,input().split()))
for i in range(t):
    k=int(input())
    a[k-1]=a[k-1]-1
for i in range(n):
    a[i]=a[i]+t
print(*a)