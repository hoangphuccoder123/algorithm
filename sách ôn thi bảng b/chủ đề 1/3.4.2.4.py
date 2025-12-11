import sys  
input=sys.stdin.readline 
n,k=map(int,input().split())
a=list(map(int,input().split()))
tong=0
prefix=[0]*(n+1)
for i in range(1,n+1):
    prefix[i]=prefix[i-1]+a[i-1]

for i in range(n):
    for j in range(i+1,n+1):
        if prefix[j]+prefix[i]<k:
            tong+=1 
print(tong)