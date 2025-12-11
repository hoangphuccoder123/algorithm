# ...existing code...
import sys 
input = sys.stdin.readline 
a = list(map(int, input().split()))

neg = []
for v in a:
    if v == 0:
        break
    if v < 0:
        neg.append(str(v))

if neg:
    print(" ".join(neg))
else:
    print("NOT FOUND")