n=int(input())
a=list(map(int,input().split()))
m=int(input())
ans=[]
for __ in range(m):
    s,f=map(int,input().split())
    count=0
    if s>f:
        s,f=f,s
    for j in range(n):
        if s<=a[j]<=f:
            count+=1
    ans.append(str(count)) 
print("\n".join(ans))