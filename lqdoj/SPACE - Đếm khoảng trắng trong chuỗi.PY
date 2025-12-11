n = int(input())

for _ in range(n):
    s = input()          # đọc nguyên dòng, kể cả space
    cnt = 0
    in_space = False     # đang ở trong một khoảng trống hay không

    for ch in s:
        if ch == ' ':
            if not in_space:   # mới bắt đầu một khoảng trống
                cnt += 1
                in_space = True
        else:
            in_space = False   # thoát khỏi khoảng trống

    print(cnt)
