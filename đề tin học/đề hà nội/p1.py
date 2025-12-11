f1=open('p1.inp','r')
f2=open('p1.out','w')
a,b,c,d=map(int,f1.readline().split())
start=[a,b,c,d]
password=[2,0,2,5]
ans=0
for i in range(4):
    x=start[i]
    t=password[i]
    cost=min(abs(x-t),10-abs(x-t))
    ans+=cost
f2.write(str(ans))
f1.close()
f2.close()