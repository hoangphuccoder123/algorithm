n=int(input())
s=0 
x=1
s2=0 # tổng bình phương = 0 
for i in range(1,n+1):
    s+=1/i 
s1=round(s,4)
print(s1)
while True:
    s2+=x**2 
    if s2 > n: 
        x-=1 
        break
    x+=1 
print(x) 
