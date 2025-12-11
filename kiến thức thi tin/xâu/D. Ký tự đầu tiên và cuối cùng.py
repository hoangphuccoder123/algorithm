import sys 
input=sys.stdin.readline
s=input().strip()
s1=input().strip()
if s[0]==s1[-1]:
    print(s[0],s1[-1],1)
else:
    print(s[0],s1[-1],0)