fi=open('p3.inp','r')
fo=open('p3.out','w')
a,b=map(int,fi.read().split())
def so_nguyen_to(n):
    if n<2:
        return False
    elif n==2:
        return True 
        for i in range(2,int(n**0.5)+1):
            if n% i==0:
                return False
        return True 

def so_dac_biet(n):
    need=int(n*n)
    if need*need == so_nguyen_to(need):
        return True 
    return False

count=0
for i in range(a,b+1):
    if so_dac_biet(i):
        count+=1
print(count)
f1=close('p3.inp')
f0=close('p3.out')