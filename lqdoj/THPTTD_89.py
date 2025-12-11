import sys 
input=sys.stdin.readline 
def snt(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False 
    return True 
n,k=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
for i in range(n):
    if snt(a[i]) and a[i]<k:
        cnt+=1
print(cnt)

