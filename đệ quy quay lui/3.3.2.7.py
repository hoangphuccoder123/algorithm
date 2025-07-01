#ham cac cac chon tien
#xay dung cac chuoi nhi phan do dai n
xau = []
def chuoiNhiPhan(i):
    for v in range(2):
        x.append(v)
        if len(x) == n:
            xau.append(x[:])
        else:
            chuoiNhiPhan(i+1)
        x.pop()
        
n, T = map(int,input().split())
t = list(map(int,input().split()))
x = []
chuoiNhiPhan(0)
for s in xau:
    tong = 0
    vitri = []
    for j in range(n):
        if s[j] == 1:
            tong += t[j]     
            vitri.append(j)
    if tong == T:
        print(*vitri)