import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
a.sort()
min_diff=float('inf')
for i in range(n):
    min_diff=min(min_diff,abs(a[i]-a[i-1]))
print(min_diff)

