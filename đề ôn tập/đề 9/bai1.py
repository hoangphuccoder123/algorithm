n=int(input())
s=0.00

x=0 



for i in range(1,n+1): 
    s+=i/(i+1) # chia số thực 
S_4_decimal = f"{s:.4f}"



while True : 
    s2=(x+1) * (x+2) * (x+3) //3 
    if s2<=n:
        x+=1
    else: 
        break
print("S =", S_4_decimal)
print("x =", x) 
