def is_amstrong(n):
    s=str(n)
    k=len(s)
    total=sum(int(c)**k for c in s)
    return total==n
n=int(input())
if is_amstrong(n):
    print(1)
else:
    print(0)