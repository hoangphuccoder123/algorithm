n=int(input())
a=list(map(int,input().split()))
a.sort()
c1=a[-1] *a[-2]*a[-3]
c2=a[0] *a[1]*a[-1]
s=max(c1,c2)
print(s)