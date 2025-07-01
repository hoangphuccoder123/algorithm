def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def phan_tich_thua_so(n):
    s = []     # Khai báo danh sách s bên ngoài vòng lặp
    i = 2
    while n > 1:
        if n % i == 0:
            s.append(i)
            n //= i
        else:
            i += 1
    return s

def tim_k(n):
    k = 1
    while True:
        if kiem_tra_so_nguyen_to(n - k):
            return k
        k += 1  

n = int(input())
s1  = phan_tich_thua_so(n)
print(f"{n} = {'.'.join(str(x) for x in s1 )}")
print("k =", tim_k(n))