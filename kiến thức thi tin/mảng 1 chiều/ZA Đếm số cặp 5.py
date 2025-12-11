import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
cnt = 0

for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        s = a[i] + a[left] + a[right]
        if s < k:
            left += 1
        elif s > k:
            right -= 1
        else:
            # s == k
            if a[left] == a[right]:
                m = right - left + 1
                cnt += m * (m - 1) // 2
                break
            else:
                # đếm số lượng trùng ở left
                cl = 1
                while left + 1 < right and a[left + 1] == a[left]:
                    cl += 1
                    left += 1

                # đếm số lượng trùng ở right
                cr = 1
                while right - 1 > left and a[right - 1] == a[right]:
                    cr += 1
                    right -= 1

                cnt += cl * cr
                left += 1
                right -= 1
        
print(cnt)
