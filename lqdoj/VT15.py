import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
a.sort()
s1=a[-1]*a[-2]*a[-3]
a2=a[0]*a[1]*a[-1]
print(max(s1,a2))