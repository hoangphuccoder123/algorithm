n = int(input())
a = list(map(int, input().split()))
s = {}
def so_nguyen_duong_nho_nhat(n):
    min_duong = float('inf')  # Better initial value for finding positives 
    for i in n: 
        if i > 0 : 
            if i < min_duong:
                min_duong = i 
    if min_duong == float('inf'):
        return "Khong co so duong" 
    return min_duong 
print("So duong nho nhat trong day:", so_nguyen_duong_nho_nhat(a)) 
for n in a:
    if n in s:
        s[n] += 1
    else:
        s[n] = 1
print("So xuat hien hon mot lan:")
found = False
for k, v in s.items():
    if v > 1:
        print(f"So {k} xuat hien {v} lan")
        found = True

if not found:
    print("Khong co so xuat hien hon mot lan")
def so_nguyen_am_lon_nhat_trong_day(n):
    max_am = float('-inf')  # Better initial value for finding negatives
    for i in n:
        if i < 0 and i > max_am:
            max_am = i
    return max_am if max_am != float('-inf') else "Khong co so am"

print("So am lon nhat trong day:", so_nguyen_am_lon_nhat_trong_day(a))