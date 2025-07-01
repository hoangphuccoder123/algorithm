a=float(input())
so_tron=abs(a) - abs(int(abs(a))) 
if so_tron >= 0.5:
    print(int(abs(a)) + 1 if a > 0 else int(abs(a)) - 1)
else:
    reuslt=int(a)
