import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
s1=min(a)
s2=max(a)
pos_min=a.index(s1)+1
pos_max=a.index(s2)+1
print(s1,pos_min,s2,pos_max)