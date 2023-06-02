import sys
lines = list(map(str.strip, sys.stdin.readlines()))

ii = 1
while ii < len(lines):
    n, m = map(int, lines[ii].split())
    ii += 1
    customers = []
    for _ in range(n):
        customers.append(list(map(int, lines[ii].split())))
        ii += 1
    customers.sort()
    curr_temp = m
    curr_time = 0
    low = curr_temp
    high = curr_temp
    for arrive, l, r in customers:
        if low - (arrive - curr_time) > r or high + (arrive - curr_time) < l:
            print("NO")
            break
        low = max(low - (arrive - curr_time), l)
        high = min(high + (arrive - curr_time), r)
        curr_time = arrive
    else:
        print("YES")


