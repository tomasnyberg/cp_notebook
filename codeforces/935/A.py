import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import math
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    a, b, c = map(int, line.split())
    missing = (3 - (b % 3)) % 3
    if c < missing:
        print(-1)
        continue
    print(a + math.ceil((b+c)/3))