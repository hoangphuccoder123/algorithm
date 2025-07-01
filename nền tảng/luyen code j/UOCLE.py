t = int(input())
for i in range(t):
    n = int(input())
    if n % 2 == 1:
        # Tìm thừa số lẻ nhỏ nhất của n
        uoc_le_max = 1
        i = 3
        while i * i <= n:
            if n % i == 0:
                uoc_le_max = n // i
                break
            i += 2
        print(uoc_le_max)
    else:
        n_chan = n 
        while n_chan % 2 == 0:
            n_chan //= 2
        
        # Fix: This if block should be inside the else block with proper indentation
        if n_chan == 1:
            print(1)  # Fix: Should be 1 instead of 11
        else:
            print(n_chan)