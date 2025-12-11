def snt(n):
    cnt=0
    if n <2:
        return False 
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            cnt+=1 
            while n%i==0:
                n//=i 
    if n>1: 
        cnt+=1 
    return cnt 
n=int(input())
s=snt(n)
print(s)