def uoc(n):
    count=0 
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            count+=1 
            if i!=n//i:
                count+=1 
    return count
def snt(n):
    if n<2:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False 
    return True
def dem_uoc_snt(n):
    count=0 
    temp=n 
    i=2 
    while i*i<=temp:
        if temp%i==0:
            count+=1
            while temp%i==0:
                temp//=i 
        i+=1 
    if temp>1:
        count+=1 
    return count
n=int(input())
a=list(map(int,input().split()))
max_uoc=-1
ket_qua=-1 
for x in a:
    so_luong=dem_uoc_snt(x)
    if so_luong > max_uoc:
        max_uoc=so_luong
        ket_qua=x
print(ket_qua)