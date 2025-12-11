import sys 
input=sys.stdin.readline 
n=input().strip()
if len(n)>1:
    digits=[int(d) for d in n]  
    s=sum(digits)
    print(s)
if len(n)==1:
    print(n)