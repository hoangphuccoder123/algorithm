def largest_divisor(n):
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def number_with_most_divisors(n):
    max_divisors = 0
    result = 1
    
    for i in range(1, n + 1):
        current_divisors = count_divisors(i)
        if current_divisors > max_divisors:
            max_divisors = current_divisors
            result = i
        elif current_divisors == max_divisors:
            result = min(result, i)
    
    return result

n = int(input())
print(f"Uoc lon nhat nho hon {n} la:", largest_divisor(n))
print(f"Tong cac chu so cua {n} la:", sum_of_digits(n))
print("So co nhieu uoc nhat la:", number_with_most_divisors(n)) 