n=int(input())
a=list(map(int,input().split()))
max_ending_here=a[0]
max_so_far=a[0]
for i in range(1,n):
    max_ending_here=max(a[i],max_ending_here+a[i])
    max_so_far=max(max_so_far,max_ending_here)
print(max_so_far)