s = input()
c = len(s)
d = 0
c = s
for i in s:
    if i.isdigit():
        d += int(i)
    
for i in c:
    if i.isdigit():
        s = s.replace(i,'')

kq = ''
for i in range(len(s)):
    if i == 0 or s[i] != s[i-1]:
        kq += s[i]

print(d)
print(kq) 