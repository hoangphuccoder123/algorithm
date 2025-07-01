def tongbp(n, k):
    a = [k] # danh sach chua so chinh 
    n -= k * k

    while n > 0:
        x = int(n ** 0.5) 
        n -= x ** 2
        a.append(x) 

    return a 

n = int(input())
kq = [] 

for k in range(int(n ** 0.5),int( (n // 2 ) ** 0.5) - 1, -1):
    b = tongbp(n,k)
    if kq == []:
        kq = b[::]
    elif len(b) < len(kq):
        kq = b[::]
    elif b[0] > kq[0] and len(b) == len(kq):
            kq = b[::]
print(kq) 