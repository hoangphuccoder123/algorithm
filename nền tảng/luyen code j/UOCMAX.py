def tim_uoc_nguyen_to_max(n):
    if n<=1:
        return 0 
    max_uoc = -1 
    while n%2==0: 
        max_uoc = 2 
        n //= 2 
    i=3
    while i*i<=n:
        while n%i==0:  
            max_uoc = i 
            n //= i
        i+=2
    if n >1 : 
        max_uoc = n
    return max_uoc
def main():
    t=int(input())
    for i in range(t):
        n=int(input()) 
        print(tim_uoc_nguyen_to_max(n)) 
if __name__ == "__main__":
    main()
