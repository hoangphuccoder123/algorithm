a,b=map(int,input().split())
if b == 0:
    print("Không thể chia cho 0")
else:
    # Tính số dư khi a chia cho b
    so_du = a % b
    print(so_du)