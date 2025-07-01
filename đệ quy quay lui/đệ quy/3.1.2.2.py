m,n=map(int,input().split())
d,r=map(int,input().split())
def dem(m,n,d,r):
    global count 
    if d==m or r==n : 
        return 1 
    else: 
        return dem(m,n,d,r) + dem(d%2, r %2 , m ,n )
count=dem(m,n,d,r)
print(count)