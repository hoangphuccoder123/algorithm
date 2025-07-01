import math 
a, b, c = map(int, input().split())
is_pythagorean = (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)
print(f"({a}; {b}; {c}) là bộ ba số Pythagoras")

ucln=math.gcd(math.gcd(a,b),c)
print(ucln)
if is_pythagorean:
    max_number = max(a, b, c)
    print(max_number)
else:
    print(f"({a}; {b}; {c}) không phải là bộ ba số Pythagoras")
