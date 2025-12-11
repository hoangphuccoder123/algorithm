n=int(input())
a=list(map(int,input().split()))
sum1=0
sum2=float('-inf')
for i in range(n):
    sum1+=a[i]
    sum2=max(sum2,sum1)
    if sum1<0:
        sum1=0 
print(sum2)
