n=int(input())
a=list(map(int,input().split()))
s=set(a)
ans=1 
while True:
    if ans not in s:
        print(ans)
        break
    ans+=1 