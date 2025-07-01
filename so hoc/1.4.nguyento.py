def check_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_tong_nguyen_to(k):
    for i in range(2, k):
        if check_so_nguyen_to(i) and check_so_nguyen_to(k-i):
            return f"{k} = {k-i} + {i}"
    return "Khong tim thay"

n = int(input())
for _ in range(n):
    k = int(input())
    print(tim_tong_nguyen_to(k))
