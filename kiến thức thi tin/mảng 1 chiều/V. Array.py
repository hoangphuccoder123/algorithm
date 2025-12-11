n=int(input())
a=list(map(int,input().split()))
s1=min(a)
print(s1)
s2=max(a)
print(s2)
s3=sum(a)
print(s3)
s4=[]
for x in a:
    if x > s1 :
        s4.append(x)
    if len(s4)<=1:
        print(-1)
    else:
        s5=min(s4)  
s5=min(s4)
print(s5)