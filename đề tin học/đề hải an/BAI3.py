import sys
input = sys.stdin.readline

def xau_doi_xung(s):
    t = s.strip()
    return t.lower() == t[::-1].lower()

k = int(input())
for _ in range(k):
    s = input().strip()
    print("YES" if xau_doi_xung(s) else "NO")

