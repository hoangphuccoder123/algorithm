import sys 
input=sys.stdin.readline
s=input().strip()
s1='q','w','ư','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'
s2='Q','W','Ư','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'
s3='1','2','3','4','5','6','7','8','9','0'
cnt1=0
cnt2=0
cnt3=0
for x in s:
    if x in s1:
        cnt1+=1 
    elif x in s2:
        cnt2+=1
    elif x in s3:
        cnt3+=1
print(cnt1)
print(cnt2)
print(cnt3)