def uoc(n):
    uoc=[]
    n=abs(n)
    if n==0:
        return None 
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            uoc.append(i)
            if i!=n//i:
                uoc.append(n//i)
    return uoc 
n=int(input())
s1=sorted(uoc(n))
ds=uoc(n)
if ds is None:
    print("INF")
else:
    s1.sort(reverse=True)
    print(*s1)