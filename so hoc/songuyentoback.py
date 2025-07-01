import math

N = int(input())

# Kiểm tra lũy thừa cao của số nguyên tố
result = 0
max_p = int(math.sqrt(N)) + 1

for p in range(2, max_p):
    # Kiểm tra tính nguyên tố nhanh hơn
    if p > 2 and p % 2 == 0:
        continue
    
    is_prime = True
    for i in range(3, int(math.sqrt(p)) + 1, 2):
        if p % i == 0:
            is_prime = False
            break
    
    if is_prime:
        power = p
        k = 1
        while power < N:
            power *= p
            k += 1
            if power == N:
                result = (p, k)
                break
        
        if result:
            break

# In kết quả
print(result[0], result[1]) if result else print(0)