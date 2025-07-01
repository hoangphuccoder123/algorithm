n=int(input())
a=list(map(int,input().split()))
a1=max(a)
a2=min(a)
s=a1-a2
print(s)
# yeu cau 2 
sorted_a=sorted(a)
min_diff=float('inf')
for i in range(len(a)-1):
    diff=abs(a[i]-a[i+1])
    if diff<min_diff:
        min_diff=diff 
print(min_diff)