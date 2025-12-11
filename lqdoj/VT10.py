import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
b=sorted(a,reverse=True)
print(*b)