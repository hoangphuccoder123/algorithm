s=input()
n=len(s)
xau=list(s)

for i in  range(n//2):
    if xau[i] =='?' and xau[n-i-1] =='?':    
        xau[i] = xau[n-i-1]='A'
    elif xau[i] =='?':
        xau[i] = xau[n-i-1] 
    elif xau[n-i-1] =='?': 
        xau[n-i-1] = xau[i]
for i in range(n//2):
    if xau[i]!=xau[n-i-1]:
        print("xâu ko có đối xứng")
        break
else:
    print("Xâu đối xứng:", ''.join(xau))