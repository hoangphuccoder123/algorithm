fi=open('p4.inp')
f0=open('p4.out','w')
n=int(fi.readline())
a=list(map(int,fi.read().split()))
count=0
if n>1:
    count +=n-1 

mang_con=[]
for i in range(n):
    while len(mang_con)>0 and a[mang_con[-1] <a[i]]: # nếu độ dài lớn 0 và phần tử cuối cùng < phần tử bất kì trong dãy con thì cho ra ngoài
        mang_con.pop()
        if len(mang_con)>0:
             count+=1
    
print(count)    
fi=close('p4.inp')
f0=close('p4.out')
