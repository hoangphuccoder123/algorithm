def snt(n):
    if n<2:
        return False 
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False 
    return True 
def scp(n):
    if n<4:
        return False
    need=int(n**0.5)
    if need*need!=n:
        return False

    return snt(need)
x,y=map(int,input().split())
cnt=0
for i in range(x,y+1):
    if scp(i):
        cnt+=1 
print(cnt)
