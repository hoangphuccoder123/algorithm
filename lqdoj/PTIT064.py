import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=a+b
s.sort()
print(*s)