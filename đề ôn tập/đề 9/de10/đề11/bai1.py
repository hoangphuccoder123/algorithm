n = int(input())
a = list(map(int, input().split()))

# Check perfect square numbers
def so_chinh_phuong(n):
    if n < 0:
        return False
    return int(n**0.5)**2 == n

print("Cac so chinh phuong trong day:", end=" ")
count = 0
for num in a:
    if so_chinh_phuong(num):
        print(num, end="; ")
        count += 1
print(f"\nCo {count} so chinh phuong")

# Numbers greater than average
def trung_binh_cong(arr):
    return sum(arr)/len(arr)

tbc = trung_binh_cong(a)
print("Cac so lon hon TBC:", end=" ")
found = False
for num in a:
    if num > tbc:
        print(num, end="; ")
        found = True
if not found:
    print("Khong co")

# Missing numbers between min and max
min_val = min(a)
max_val = max(a)
print("\nCac so khong thuoc day:", end=" ")
found = False
for i in range(min_val, max_val + 1):
    if i not in a:
        print(i, end="; ")
        found = True
if not found:
    print("Khong co") 