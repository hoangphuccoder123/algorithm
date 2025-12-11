import sys
input = sys.stdin.readline

n = int(input())
freq = {}

for _ in range(n):
    s = input().strip()
    if s in freq:
        freq[s] += 1      # nếu đã có thì tăng đếm
    else:
        freq[s] = 1       # nếu chưa có thì gán = 1

# in ra theo thứ tự từ điển
for s in sorted(freq.keys()):
    print(s, freq[s])
 
