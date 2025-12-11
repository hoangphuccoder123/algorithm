import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))
ds_le=[]
for i in range(n):
    if a[i]%2==1:
        ds_le.append(a[i])
        tbc=sum(ds_le)/len(ds_le)
print(f"{tbc:.4f}")