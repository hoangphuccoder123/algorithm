n=int(input())
a=list(map(int,input().split()))
s1=max(a)
s2=min(a)
cnt1=0
cnt2=0
for i in range(n):
    if a[i]==s1:
        cnt1+=1
    elif a[i]==s2:
        cnt2+=1

print(s2,cnt2)
print(s1,cnt1)