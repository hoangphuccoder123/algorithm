import math

def min_actions(x):
    # Tính số bit "hiệu dụng" của x
    num_bits = math.floor(math.log2(x)) + 1
    # Áp dụng công thức 2 * num_bits + 1
    return 2 * num_bits + 1

t = int(input())
for _ in range(t):
    x = int(input())
    print(min_actions(x)) 