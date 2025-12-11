import sys 
input=sys.stdin.readline 
def snt(n):
    if n<2: return False 
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False 
    return True 
n=int(input())
a=list(map(int,input().split()))
b=sorted(set(a))
for i in b:
    if snt(i):
        print(i,end=" ")