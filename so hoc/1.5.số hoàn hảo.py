def check_so_hoan_hao(n):
    if n < 2:
        return False
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n

def in_uoc(n):
    print(f"Các ước của {n} là:", end=" ")
    for i in range(1, n):
        if n % i == 0:
            print(i, end=" ")
    print()

n = int(input())
if n < 10 or n > 99:
    print("Hãy nhập số có 2 chữ số!")
else:
    if check_so_hoan_hao(n):
        print(f"{n} là số hoàn hảo")
        in_uoc(n)
    else:
        print(f"{n} không phải là số hoàn hảo")
