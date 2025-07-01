n=int(input())
sang_so=[True]*(n+1)
sang_so[0]=sang_so[1]=False
i=2 
while i*i<=n:
    if sang_so[i]:
        for j in range(i*i,n+1,i):
            sang_so[j]=False
    i+=1
sang_so_list=[]
for i in range(2,n+1):
    if sang_so[i]:
        sang_so_list.append(i)
print(*sang_so_list)
