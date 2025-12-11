n=int(input())
a=list(map(int,input().split()))
b=a[0]

for i in range(1,n):
    if a[i] < b:
        b=a[i]

for i in range(n):
    if a[i] ==b:
        print(i+1,end=' ')