fi=open('p1.inp')
fo=open('p1.out','w')
n=int(fi.read())
import math
def tim_uoc(n):
    uoc = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            uoc.append(i)
            if i != n // i:
                uoc.append(n // i)
    return sorted(uoc)
min_diff=float('inf')
for i in range(1,int(math.sqrt(n))+1):
    if n %i==0 : 
        a=i 
        b=n//i
        diff=abs(a-b)
        if diff < min_diff:
            min_diff=diff
fo.write(f'{min_diff}')