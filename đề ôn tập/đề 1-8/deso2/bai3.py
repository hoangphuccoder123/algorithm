s=input()
total_digits=0 
for char in s : 
    if char.isdigit():
        total_digits+=int(char)
s1=""
for char in s: 
    if not  char.isdigit():
        s1+=char
s2 = s1[0] if s1 else "" 
for i in range(1,len(s1)):
    if s1[i]!= s1 [-1]:
        s2+=s1[i]
print(s1)
print(s2)  
print(total_digits)