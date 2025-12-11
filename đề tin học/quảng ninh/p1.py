fi=open('P1.INP','r')
fo=open('P1.OUT','w')
n=int(fi.readline().strip())
counts={}
for _ in range(n):
    name=fi.readline().strip()
    if name not in counts:
        counts[name]=0
        fo.write(name+'\n')
    else:
        counts[name]+=1 
        fo.write(name + str(counts[name]) + '\n')
fi.close()
fo.close()  