a, b, c = map(int, input().split())

if a <= 0 or b <= 0 or c <= 0:
    print(f"{a}; {b}; {c} khong la 3 canh cua tam giac")
elif (a + b > c) and (a + c > b) and (b + c > a):
    print(f"{a}; {b}; {c} la 3 canh cua tam giac")
    # Calculate area using Heron's formula
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"Dien tich cua tam giac la: {s:.2f}")
    
    # Determine triangle type using Pythagorean theorem
    sides = sorted([a, b, c])
    a2, b2, c2 = sides[0]**2, sides[1]**2, sides[2]**2
    
    if a2 + b2 == c2:
        print("Day la mot tam giac vuong")
    elif a2 + b2 > c2:
        print("Day la mot tam giac nhon")
    else:
        print("Day la mot tam giac tu")
else:
    print(f"{a}; {b}; {c} khong la 3 canh cua tam giac") 