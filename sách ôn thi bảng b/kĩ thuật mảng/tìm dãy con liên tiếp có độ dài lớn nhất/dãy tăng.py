import sys
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
res=0
cnt=1
b=[]
for i in range(1,n):
    if a[i]>a[i-1]:
        cnt+=1 
    else:
        cnt=1 
    res=max(res,cnt)
print(res)