def tim_uoc(n):
    uoc=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            uoc.append(i)
            if i!=n//i:
                uoc.append(n//i)
    return uoc 
def so_hoan_hao(n):
    if n<1:return False
    tong=0
    for i in tim_uoc(n):
        if i!=n:
            tong+=i
    return tong==n
n=int(input())
if so_hoan_hao(n):
    print("YES")
else:
    print("NO")