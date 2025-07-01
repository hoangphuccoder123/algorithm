
from functools import lru_cache
@lru_cache(maxsize=100)
def compute_heavy_function(x):
    # A computationally expensive operation
    return x ** x
import gc
# Manual garbage collection to free up memory
large_data = [i for i in range(1000000)]
del large_data
gc.collect()  # Forces garbage collection
def is_happy_number(n):   
    seen = set()  # To track numbers we've seen
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))  # Calculate sum of squares of digits
    return n == 1  # Return True if n is 1, else False

def count_happy_numbers(a, b):
    count = 0
    for i in range(a, b + 1):
        if is_happy_number(i):  # Check if i is a happy number
            count += 1
    return count

# Input handling
n = int(input("Enter number of test cases: "))  # Number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(n)]  # List of (a, b) pairs

# Process each test case
for a, b in test_cases:
    print(count_happy_numbers(a, b))  # Print the count of happy numbers in the range [a, b]