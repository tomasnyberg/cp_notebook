import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from math import gcd
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    x = int(line)
    result = [-1,-1]
    for y in range(1, x):
        result = max(result, [gcd(x, y) + y, y])
    print(result[1])
