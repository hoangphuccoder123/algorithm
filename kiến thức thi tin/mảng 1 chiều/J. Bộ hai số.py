n=int(input())
a=list(map(int,input().split()))
count=0
for  i in range(n-1):
    if a[i]*a[i+1]>0:
        count+=1
    elif a[i]==a[i+1]:
        count+=0
    else: 
        count+=0 
print(count)