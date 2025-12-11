fi=open('p1.inp','r')
fo=open('p1.out','w')
n=int(fi.readline())
b=list(map(int,fi.read().split()))
a=[0]*n
prefix_sum=0
for i in range(n):
    a[i]=(i+1)*b[i]-prefix_sum
    prefix_sum+=a[i]
fo.write(' '.join(map(str, a)))
fi.close()
fo.close()
