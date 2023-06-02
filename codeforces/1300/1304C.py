import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check_same_time_bad(customers):
    i = 0
    while i < len(customers):
        arrive, low, high = customers[i]
        i += 1
        while i < len(customers) and customers[i][0] == arrive:
            _, low_b, high_b = customers[i]
            if low_b > high or high_b < low:
                return True
            low = max(low, low_b)
            high = min(high, high_b)
            i += 1
    return False

ii = 1
while ii < len(lines):
    n, m = map(int, lines[ii].split())
    ii += 1
    customers = []
    for _ in range(n):
        customers.append(list(map(int, lines[ii].split())))
        ii += 1
    customers.sort()
    if check_same_time_bad(customers):
        print("NO")
        continue
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


