import sys 
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
s=[]
removed=[False]
for i in range(len(a)):
    if removed[i]:
        continue
    for j in range(i+1,len(a)):
        if removed[j]:
            continue
        if (a[i]!=0 and a[j]%a[i]==0) or(a[j]!=0 and a[i]%a[j]==0):
            removed[i]=True 
            removed[j]=True 
            s.append(i*j)
print(len(s))