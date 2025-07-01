def so_nguyen_to(n): 
    if n<2:
        return False 
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False 
    return True
n=int(input()) 
a=list(map(int,input().split()))
print("Cac so nguyen to trong day:", end=" ") 
for num in a:
    if so_nguyen_to(num):
        print(num, end=" ")
        found=True
if not found: 
    print("Khong co so nguyen to nao trong day") 

max_len=0
max_sum=0
max_seq=[] 
current=[]
for num in a: 
    if so_nguyen_to(num):
        current.append(num)
        if len(current)>max_len:
            max_len=len(current)
            max_seq=current 
            max_sun+=num
        elif len(current)==max_len: 
            if sum(current)>max_sun:
                max_seq=current 
                max_sun=sum(current) 
        else:
            current=[] 
if len(current) > max_len:
    max_seq = current
elif len(current) == max_len and sum(current) > max_sum:
    max_seq = current

print("\nDay so nguyen to lien tiep dai nhat:", end=" ")
if max_seq:
    print(*max_seq)
else:
    print("Khong co day so nguyen to lien tiep")