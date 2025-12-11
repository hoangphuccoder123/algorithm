a,b,c,d=map(int,input().split())
cnt=0 
for i in range(min(a,c),max(b,d)+1):
    if a<=i<=c and b<=i<=d:
        cnt+=1 
print(cnt)