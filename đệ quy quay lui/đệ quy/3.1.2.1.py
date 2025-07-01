d,c=map(int,input().split())
i,j=map(int,input().split())
def dem(i,j,d,c):
    global count 
    if i ==d or i == c:
        return 1 
    else:
        return dem(i,j,d,c) + dem(i,j+1,d,c)
count=dem(i,j,d,c)
print(count)