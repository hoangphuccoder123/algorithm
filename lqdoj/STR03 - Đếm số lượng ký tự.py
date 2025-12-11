s=input()
t=int(input())
for _ in range(t):
    x=input()
    if not x :
        print(0)
    else:
        print(s.count(x))