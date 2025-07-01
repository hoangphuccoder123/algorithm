n, m = map(int, input().split())

if 2 < m < 10**6 and 1 < n < 45:
    s = []
    
    for i in range(2, m):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            s.append(i)
    
    print(s)
else:
    print("Giá trị m hoặc n không hợp lệ!")
