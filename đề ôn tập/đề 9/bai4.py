n = input()
s = []
current = n

while len(current) > 1:
    s1 = 0
    for i in current:
        s1 += int(i)  
    s.append(s1)
    current = str(s1)

print("Day so:", end=" ")
print(*s) 