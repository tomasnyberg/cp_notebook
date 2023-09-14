import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict


for line in lines[1:]:
    a, b = map(int, line.split())
    if b < 4:
        print(-1)
        continue
    if a < 4:
        a = 4
    if b - a >= 1:
        if a % 2 == 1:
            a += 1
        print(a-2, 2)
        continue
    found = False
    for i in range(2, int(math.sqrt(a)) + 5):
        if i >= b: break
        if b % i == 0:
            found = True
            print(i, b - i)
            break
    if not found:
        print(-1)

