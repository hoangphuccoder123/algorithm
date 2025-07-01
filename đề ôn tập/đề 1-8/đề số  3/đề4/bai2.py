n=int(input())
a=list(map(int,input().split()))
so_tang_dan=sorted(a)
print(so_tang_dan)
b=[]
for x in a: 
    if  x % 2 == 0:
        b.append(x-3)
    else:
        b.append(x+5)
g=sorted(b)
print(g)  
    