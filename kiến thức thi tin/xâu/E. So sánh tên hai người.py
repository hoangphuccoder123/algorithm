import sys 
input=sys.stdin.readline 
s1=input().strip()
s2=input().strip()
if len(s1)>len(s2):
    print(s1)
else:
    print(s2)