import sys 
input=sys.stdin.readline 
s=input().strip()
freq={}
for x in s:
    if x in freq:
        freq[x]+=1 
    else:
        freq[x]=1
if not freq:
    print()
candidates=[x for x,f in freq.items() if f==max_freq]
if len(candidates)==1:
    print(candidates[0])
else:
    print(*candidates)
max_freq=max(freq.values())
print(x,max_freq)