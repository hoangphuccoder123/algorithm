n=int(input())
for k in range(n):
    s=input().strip()
    max_len=0
    curr=0 
    for char in s :
        if char =='W' or char=="A" or char=="R":
            curr+=1 
            if cur>max_len:
                max_len=curr
        else:
            curr=0 
    


    print(curr)