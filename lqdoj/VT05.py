import sys
input=sys.stdin.readline
n,x=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in range(n):
    if a[i]==x:
        count+=1 
print(count)