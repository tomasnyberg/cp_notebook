import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(a, b):
    a, b = min(a, b), max(a, b)
    result = 10**25
    for length in range(1, 10000):
        lencost = length - 1
        bcost = 1 + b // length
        acost = 1 if a <= length else 1 + a // length
        result = min(result, lencost + bcost + acost)
    return result - 1

for line in lines[1:]:
    a, b = map(int, line.split())
    print(solve(a, b))
    # print(result)
