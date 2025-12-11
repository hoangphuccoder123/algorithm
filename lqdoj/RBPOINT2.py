import sys
input=sys.stdin.readline
n=int(input())
b=list(map(int,input().split()))
r=list(map(int,input().split()))
min_diff=float('inf')
if len(b) and len(r)==1:
    min_diff=abs(b[0]-r[0])
    print(min_diff)
for i in range(n):
    min_diff=min(min_diff,abs(b[i]-r[1]))
print(min_diff)