import sys 
input=sys.stdin.readline 
a=list(map(int,input().split()))

if len(a) < 11:
    print(-1)
else:
    target=a[10]
    print(*[i + 1 for i, v in enumerate(a) if v == target]) 