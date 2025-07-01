n=int(input())
mod=1e9*7 
m=n//3 
r=n% 3
if r==0:
    s1=3*m*(m-1) //2
elif r==1 :
    s1=3*m*(m-1) //2 +(3*m+1)
elif r==2:
    s1=3*(m+1)*(m+2)//2 
print(s1)
print(round(4))