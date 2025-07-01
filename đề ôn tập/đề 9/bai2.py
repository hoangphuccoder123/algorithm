n=int(input())
a=list(map(int,input().split()))
arr=[]
max_arr=max(a)
print(max_arr)
# yeu cau 2 
even_arr=[i for i in a if i%2==0 and i>0] 
print(" ; ".join(map(str, even_arr))) 
# yeu cau 3
def day_dan(arr):
    for i in range(len(arr)-1): 
        if(arr[i]>0 and arr[i+1]>0 ) or(arr[i]<0 and arr[i+1]<0):
            return False
    return True 
if day_dan(a):
    print("YES") 
else: 
    print("NO") 

