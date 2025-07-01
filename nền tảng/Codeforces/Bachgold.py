n = int(input())

if n % 2 == 0:
    # n là số chẵn
    print(n // 2)
    print("2 " * (n // 2))
else:
    # n là số lẻ
    print(n // 2)
    print("2 " * (n // 2 - 1) + "3") 