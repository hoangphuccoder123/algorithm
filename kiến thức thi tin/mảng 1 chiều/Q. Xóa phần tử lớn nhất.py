n=int(input())
a=list(map(int,input().split()))
s=max(a)
s1=[]
for i in range(n):
    if a[i]!=s:
        s1.append(a[i])
print(*s1)