import sys 
input=sys.stdin.readline 
a=list(map(int,input().split()))
s=[]
for x in a:
    if x>=1:
        s.append(x)
print(s)