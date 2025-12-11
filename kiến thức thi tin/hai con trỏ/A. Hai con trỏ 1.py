n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=0
j=0
c=[]
while i<n and j<m:
    if a[i]<b[j]:
        c.append(a[i])
        i+=1 
    else:
        c.append(b[j])
        j+=1 
while i<n:
    c.append(a[i])
    i+=1 
while j<m:
    c.append(b[j])
print(*c)