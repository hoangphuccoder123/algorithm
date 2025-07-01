n = int(input())
dem = 0
for i in range(1,n+1):
    if n%i==0:
        dem += 1
s = str(n) 
k = len(s)
max_digit = max(int(x) for x in s)
digits = sorted([int(x) for x in s], reverse=True)
max_num = int(''.join(map(str,digits)))
print(dem) 
print(k)
print(max_digit)
print(max_num)
