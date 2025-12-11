def snt(n):
    if n<2: return False 
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False 
    return True 

def tong_uoc(n):
    s=0
    i=1
    while i*i<=n:
        if n % i==0:
            if i*i==n:
                s+=i
            else:
                s+=i+n//i
        i+=1
    return s
n=int(input())
cnt=0
for x in range(1,n+1):
    if snt(tong_uoc(x)):
        cnt+=1 
print(cnt)