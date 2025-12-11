fi=open('p2.inp','r')
fo=open('p2.out','w')
n,l,r=map(int,fi.readline().split())
a=list(map(int,fi.read().split()))
d=[]
tong=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        tong=a[i]+a[j]
        if l<=tong<=r:
            d.append(tong)
            s1=min(d)
fo.write(str(s1))
fi.close()
fo.close()