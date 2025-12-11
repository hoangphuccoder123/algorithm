# KIỂM TRA SỐ CHÍNH PHƯƠNG 
def snt(n):
    if n<2:return False 
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False 
    return True 
def so_chinh_phuong(n):
    need=int(n**0.5)
    if need**2==n:return True 
    return False 
n=int(input())
if so_chinh_phuong(n):
    print("YES")
else:
    print("NO")