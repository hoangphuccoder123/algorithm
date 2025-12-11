import sys 
input=sys.stdin.readline 
a,b,c=map(int,input().split())
s1=a*b
s2=(a-c)*c
s3=b*c
s4=s1-s2-s3
print(s4)