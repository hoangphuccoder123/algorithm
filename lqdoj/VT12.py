import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
s1=max(a)
s2=min(a)
print(abs(s1-s2))