n=int(input())
a=list(map(int,input().split()))
def so_nguyen_to(n):
    if n<2:
        return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False 
        return True 
def so_chinh_phuong(n):
    so_can=int(n**0.5)
    if so_can*so_can!=n:
        return False 
    return True 
count=0 
for i in range(n):
    if so_chinh_phuong(a[i]):
        count+=1 

print(count)