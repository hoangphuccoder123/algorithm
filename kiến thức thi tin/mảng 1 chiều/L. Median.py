n=int(input())
a=list(map(int,input().split()))
a.sort()
b=a
count=0
mid=n//2
if n%2==1:
    median=a[mid]
else:
    median = (a[mid - 1] + a[mid]) / 2
if median == int(median):
    print(int(median))
else:
    print(median)