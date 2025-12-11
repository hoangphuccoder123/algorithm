import sys, math
input = sys.stdin.readline

n = int(input().strip())
limit = math.isqrt(n)  # count primes p with p^2 <= n  => p <= isqrt(n)

if limit < 2:
    print(0)
else:
    is_prime = [True] * (limit + 1)
    if limit >= 0: is_prime[0] = False
    if limit >= 1: is_prime[1] = False

    up = int(limit ** 0.5)
    for p in range(2, up + 1):
        if is_prime[p]:
            step = p * p
            for q in range(step, limit + 1, p):
                is_prime[q] = False

    print(sum(is_prime))