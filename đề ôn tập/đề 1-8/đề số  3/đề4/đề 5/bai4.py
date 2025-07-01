n,k=map(int,input().split())
a=list(map(int,input().split()))
b=a.sort()
print(a.sort())
d={}
c=[]
for i in range(n):
    if a[i] in d : 
       d[a[i]]+=1
    else:
        d[a[i]]=1
c=[x for x in d if d[x] > k ]
print(sorted(c)) 