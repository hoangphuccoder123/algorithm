import sys
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
b=sorted(set(a))
print(b[-1],b[-2])