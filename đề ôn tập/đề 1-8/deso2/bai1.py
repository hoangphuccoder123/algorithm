n=int(input())
print(len(str(n)))
print(sum([int(i) for i in str(n)]))
print(sum(i for i in range(2,n) if all(i%j!=0 for j in range(2,int(i**0.5)+1))))
x=n-1 
while not all(x& j for j in range(2,int(x**0.5)+1)):
    x-=1
print(x)