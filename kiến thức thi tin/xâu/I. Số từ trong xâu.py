import sys 
input=sys.stdin.readline
s=input().strip()
cnt=0 
words=s.split()
for x in words:
    cnt+=1
print(cnt)