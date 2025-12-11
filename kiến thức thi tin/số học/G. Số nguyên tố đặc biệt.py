def snt(n):
    if n<2:
        return False  
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False 
    return True
def tong_chu_so(n):
    return sum(int(x) for x in str(n))
s=[]
l,r=map(int,input().split())
for i in range(l,r+1):
    if snt(i) and snt(tong_chu_so(i)):
        s.append(i)
print(*s)
        
