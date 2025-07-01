def backtrack(i):
    for v in range(2):
        x.append(v)
        if i==n-1:
            print(x)
        else: 
            backtrack(i+1)
    x.pop()
n=int(input())
x=[]
backtrack(0)