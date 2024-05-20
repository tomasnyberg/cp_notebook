import math
import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    x, y = map(int, line.split())
    min_by_two = math.ceil(y/2)
    extra_available = min_by_two * 7 + (4 if y % 2 == 1 else 0)
    if extra_available >= x:
        print(min_by_two)
    else:
        print(min_by_two + math.ceil((x - extra_available) / 15))
