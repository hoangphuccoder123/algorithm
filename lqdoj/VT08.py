import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
for i in range(1,n,2):
    left=a[-1]
    right=a[i+1] if (i+1<n) else 0 
    chenh_lech=abs(left-right)
    a[i]+=chenh_lech
print(*a)