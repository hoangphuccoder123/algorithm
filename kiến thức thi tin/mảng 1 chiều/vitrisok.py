n=int(input())
a=list(map(int,input().split()))
k=int(input())
found=False 
for i in range(n):
    if a[i]==k:
        print(i+1,end=" ")
        found=True 
if not found:
    print(-1)