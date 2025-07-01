def tinhtong(a):
    n = len(a)
    dp = [0] * (n+1)
    dp[0] = a[0]
    for i in range(1, n):
        dp[i] = max( a[i],dp[i-1]+a[i] )

    return dp[n - 1]

n = int(input())
a = list(map(int,input().split()))
m = int(input())

for i in range(0, m):
    x, y = map(int,input().split())
    b = a[x- 1: y ]

    print(tinhtong(b))