
n, m = map(int, input().split())
l= [tuple(map(int, input().split())) for _ in range(n)]
dp=[0]*(m+1)
for i ,l in l : 
    for j in range(m,i -1,-1):
        dp[j]=max(dp[j],dp[j-i]+l)
        print(dp[m])
    