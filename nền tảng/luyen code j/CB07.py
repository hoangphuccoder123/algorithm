r=float(input())
if r < 0 or r > 100:
    print("Khong hop le") 
else:
    pi = 3.14 
    s = pi * r * r
    chu_vi = 2 * pi * r
    print(f"{chu_vi:.3f} {s:.3f}")
