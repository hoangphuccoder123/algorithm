a,b=map(int,input().split())
if a!=0:
    print(f"{-b/a:.2f}")
elif a==0 and b!=0:
    print("NO")
else:
    print("WOW")