import sys
input=sys.stdin.readline
n=int(input())
segments=[]
for _ in range(n):
    l,r=map(int,input().split())
    segments.append((r,l))
segments.sort()
for r , l in segments:
    print(l,r) 
