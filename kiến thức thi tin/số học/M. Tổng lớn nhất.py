n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
s1=max(a)
s2=min(a)
s=[]
for i in range(n):
    if a[i]!=s1 and a[i]!=s2:
        s.append(i)
s3=max(s)
s4=min(s)
if s1+s3  