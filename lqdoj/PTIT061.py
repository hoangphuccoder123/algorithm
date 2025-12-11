# ...existing code...
import sys 
input=sys.stdin.readline 
n=int(input())
a=list(map(int,input().split()))

def max_digits_value(x):
    s = list(str(abs(x)))
    if x >= 0:
        s_sorted = sorted(s, reverse=True)   # lớn nhất: sắp xếp giảm dần
        return int(''.join(s_sorted))
    else:
        s_sorted = sorted(s)                 # âm: để giá trị (ít âm) lớn nhất, giảm |x| → sắp xếp tăng dần
        return -int(''.join(s_sorted))

b = [max_digits_value(x) for x in a]
b.sort(reverse=True)   # in theo chiều không tăng
print(*b)
# ...existing code... 