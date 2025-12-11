import sys 
input=sys.stdin.readline 
def sang_nguyen_to(n):
    snt=[True]*(n+1)
    snt[0]=snt[1]=False 
    for i in range(2,int(n**0.5)+1):
            
def tim_uoc(n):
    uoc=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            uoc.append(i)
            if i!=n//i:
                uoc.append(n//i)
    return uoc 
def snt(n):
    if n<2:return False 
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False 
    return True 

n=int(input())
cnt=0
for i in range(n):
    if snt(a[i]*a[i+1])
print(cnt)