n,t=map(int,input().split())
p=list(map(int,input().split()))
s=list(map(int,input().split())) 
k=-1
d=(-1,-1)
for i in range(n): 
    for j in range(i+1,n):
        if p[i]+p[j]<= t : 
            s1=s[i]+s[j]
            if s1 >k : 
                d =(i ,j)
print(k)
print(d[0]+1,k[0]+1)

        