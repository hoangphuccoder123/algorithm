import math 
n=int(input())
if n < 1: 
    print("No")
    exit()
s1=int(math.sqrt(n))**2
print(s1)
if(n&(n-1)) ==0: 
    print("lũy thừa của 2 ")
else:
    print("không phải lũy thừa của 2 ")
x=int(math.log2(n))
y=n-(2**x)
print(x,y)    