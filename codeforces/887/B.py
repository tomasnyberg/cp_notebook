import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    n, k = map(int, line.split())
    if k > 46:
        print(0)
        continue
    count = 0
    for x in range((n // 2) + 1):
        y = n - x
        valid = True
        for _ in range(k - 2):
            x, y = y - x, x
            if x < 0:
                valid = False
                break
        if valid:
            count += 1
    print(count)