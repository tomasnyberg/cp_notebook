import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, m, k = list(map(int, line.split(" ")))
    # print(n, m, "horizontal:", k, "vertical:", (n*m)//2 -k)
    if n % 2 == 1: # We need to make 
        needed_for_col = m//2
        print("YES" if k >= m//2 and (k - needed_for_col)%2 == 0 else "NO")
    elif m % 2 == 1:
        needed_for_row = n // 2
        amount = (n*m)//2 -k
        print("YES" if amount >= n // 2 and (amount - needed_for_row)%2==0 else "NO")
    else:
        print("YES" if k%2 == 0 else "NO")