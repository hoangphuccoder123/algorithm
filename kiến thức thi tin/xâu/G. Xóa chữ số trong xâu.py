import sys 
input=sys.stdin.readline 
s=input().strip()
so='1','2','3','4','5','6','7','8','9','0'
kq=""
for x in s:
    if x not in so:
        kq+=x
print(kq)