n = int(input())  
s = 0  

if n == 1:
    s = 10000
elif 2 <= n <= 10:
    s = 10000 + (n - 1) * 9000
elif n > 10  :
    s = 10000 + 9 * 9000 + (n - 10) * 8000
if n > 50:
    s=s*0.9

print(int(s))

