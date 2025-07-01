n,k=map(int,input().split())
count=len(str(abs(n))) 
print(count)
if count<k:
    print(0)
else: 
    count = int(str(n)[:-k] ) 
    if n < 0 :
        count = -count 
    print(count) 
def so_nguyen_to(n): 
    if n<2:
        return False 
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False 
    return True
n_str=str(abs(n))
found=False
for i in range(len(n_str)):
    n1 = int(n_str[:-i]) if i > 0 else abs(n)
    if n<0 :
        n1=-n1 
    if so_nguyen_to(n1): 
        print(n1)
        break 
