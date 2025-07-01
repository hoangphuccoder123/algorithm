def lietkehoanvi(n): 
    for i in range(l):
        if not (v in x):
            x.append(v)
            if i == n-1: 
                print(x)
            else: 
                lietkehoanvi(n+1) 
            x.pop()
n=int(input())
x=[]
lietkehoanvi(00