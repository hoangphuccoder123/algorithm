import sys 
def kandee(n):
    max_ending_here=0 
    max_so_far=float('-inf')
    for x in n:
        max_ending_here=max(max_ending_here+x,x)
        max_so_far=max(max_so_far,max_ending_here)
    return max_so_far

n=int(input())
a=list(map(int,sys.stdin.readline().split()))
print(kandee(a))