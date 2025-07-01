def gcd(a, b):
    if a == 0 or b == 0:
        return a + b
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a 
def rut_gon(c,d):
    uoc=gcd(abs(c),abs(d))
    return c//uoc,d//uoc 
a,b,c,d=map(int,input().split())
tong_tu= a*d + b*c 
tong_mau= b*d
tong_tu,tong_mau=rut_gon(tong_tu,tong_mau)
print(tong_tu,tong_mau)