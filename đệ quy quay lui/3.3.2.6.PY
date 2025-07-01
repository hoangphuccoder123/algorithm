D = int(input("Nhập dung lượng của mỗi ổ cứng (Mb): "))
n = int(input("Nhập số lượng file dữ liệu: "))
sizes = list(map(int, input("Nhập kích thước của các file dữ liệu (Mb), cách nhau bởi dấu cách: ").split()))
sizes = sorted(enumerate(sizes), key=lambda x: x[1], reverse=True)
disk1 = []
disk2 = []
size1 = 0
size2 = 0
for i, size in sizes:
    if size1 + size <= D:
        disk1.append(i)
        size1 += size
    elif size2 + size <= D:
        disk2.append(i)
        size2 += size
store = [0] * len(sizes)
for i in disk1:
    store[i] = 1
for i in disk2:
    store[i] = 2
print("Phương án lưu trữ:", store)