fi=open('p1.inp')
fo=open('p1.out','w')
s=fi.read().strip()
cnt=0
result=''
for char in fi.read():
    if c.count(char) ==1:
        resullt=char 
        cnt+=1 
        break 
fo.write(cnt)
f1.close()
f0.close()
        