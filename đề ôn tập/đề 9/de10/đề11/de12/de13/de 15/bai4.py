n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
print(a)
def so_nguyen_to(n):
    if n<2:
        return False 
    for i in range(2,int(n**0.5)+1):
        if n % i ==0 :
            return False
        return True 
s1=max_len=00# độ dài dãy con 
s2 =max_start= 0 # vị trí bắt đầu để duyệt
for i in range(len(a)):
    if so_nguyen_to(a[i]):
        if s1==0:
            s2=i
        s1+=i
        if s1 > s2:
            s1=max_len
            s2=max_start

    else: 
        s1=0
print("Day duoc sap xep giam dan la:", ", ".join(map(str, a)))
if max_len > 0:
    result = a[max_start:max_start + max_len]
    print("Day con nguyen to lon nhat:", ", ".join(map(str, result)))
else:
    print("Khong co day con nguyen to")