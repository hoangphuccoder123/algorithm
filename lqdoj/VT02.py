n = int(input())
a = list(map(int, input().split()))

if n < 2:
    print("NOT FOUND")  # hoặc -1 tùy đề yêu cầu
else:
    max1 = a[0]      # số lớn nhất
    max2 = None      # số lớn thứ 2 (khác max1)

    for x in a[1:]:
        if x > max1:
            max2 = max1
            max1 = x
        elif x < max1:
            if max2 is None or x > max2:
                max2 = x

    if max2 is None:
        print("NOT FOUND")  # không có giá trị lớn thứ 2 (ví dụ: 5 5 5)
    else:
        print(max2)
 