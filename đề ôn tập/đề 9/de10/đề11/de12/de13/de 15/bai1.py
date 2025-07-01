m,n,p = map(int,input().split())

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def lcm(a,b):
    return abs(a*b)//gcd(a,b)

def so_lon_nhat(m,n,p):
    return max(m,n,p)

def so_nho_nhat(m,n,p):
    return min(m,n,p)

def gcdmax_min(m,n,p):
    max_num = so_lon_nhat(m,n,p)
    min_num = so_nho_nhat(m,n,p)
    return gcd(max_num,min_num)

def lcmmax_min(m,n,p):
    max_num = so_lon_nhat(m,n,p)
    min_num = so_nho_nhat(m,n,p)
    return lcm(max_num,min_num)

print(so_lon_nhat(m,n,p))
print(so_nho_nhat(m,n,p))
print(gcdmax_min(m,n,p))
print(lcmmax_min(m,n,p))