n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
s=[]
for x in b:
    if x>0:
        s.append(x)
print(len(s))