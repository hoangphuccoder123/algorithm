import sys 
input=sys.stdin.readline 
t=int(input())
chuoi='Happy New Year!!!'
for _ in range(t):
    s=input().strip()
    if chuoi in s:
        print("YES")
    else:
        print("NO")
