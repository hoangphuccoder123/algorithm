fi=open('p2.inp')
fo=open('p2.out','w')
n=int(fi.readline())
a=list(map(int,fi.read().split()))
s=min(a)
count=0
for i in a:
    if s==i:
        count+=1 
print(s,count)