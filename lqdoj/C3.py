import sys 
input=sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
seen={}
for x in a :
    target=k-x*x
    cnt+=seen.get(target,0)
    seen[x]=seen.get(x,0)+1
print(cnt)