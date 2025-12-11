def so_nguyen_to(n):
    if n<2:
        return False 
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False 
    return True 
n=int(input())
a=list(map(int,input().split()))
for i in range(1,n+1):
    if so_nguyen_to(a[i]):
        print(i,end=' ')