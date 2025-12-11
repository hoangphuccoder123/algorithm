import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
a.sort()
q=int(input())
for _ in range(q):
    x=int(input())
    # lower_bound: chỉ số đầu tiên i sao cho a[i] >= x
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    i = lo
    if i == 0:
        print(-1)
    else:
        print(a[i-1])