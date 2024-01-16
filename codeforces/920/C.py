import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, f, a, b = list(map(int, lines[ii].split()))
    nums = list(map(int, lines[ii+1].split()))
    # Lose A at every unit of time
    # turn off and turn on later for cost B
    # can send and turn off same moment
    nums.sort()
    prev = 0
    for x in nums:
        diff = x - prev
        prev = x
        if diff * a > b:
            f -= b
        else:
            f -= diff * a
        if f <= 0:
            print('NO')
            break
    else:
        print('YES')