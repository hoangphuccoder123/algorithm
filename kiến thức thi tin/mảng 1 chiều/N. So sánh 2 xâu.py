n=int(input())
for i in range(n):
    s1=input().strip()
    s2=input().strip()
    if len(s1)>len(s2):
        print(1)
    else:
        print(0)