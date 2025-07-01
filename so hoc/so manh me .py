import math 

def snt(x):
    if x < 2 :
        return False
    else : 
        for i in range(2,x):
            if x % i == 0 :
                return False
    return True
a = []
for i in range (1,100) :
    if snt(i)  == True :
        for j  in range(1,100):
            if j % i == 0 and j% i **2 ==0 :
                a.append(j)
def loai(lst):
    return list(set(lst)) 
 
print(*loai(a)  )