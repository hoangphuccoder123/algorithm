def mat_khau(n):
    if len(n)<6:return False 
    d1=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","v","b","n","m"]
    d2=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    d3=['1','2','3','4','5','6','7','8','9']
    if any(c in d1 for c in n) and any(c in d2 for c in n ) and ( c in d3 for c in n):
        return True 
    return False 

n=input()
count=0
for i in range(len(n)):
    for j in range(i+5,len(n)):
        sub=n[i:j+1]
        if mat_khau(sub):
            count+=1 
print(count)