import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(a, b):
    a, b = min(a, b), max(a, b)
    result = 10**25
    for length in range(1, min(b, 10**5) + 1):
        lencost = length - 1
        bcost = 1 + b // length if b % length != 0 else b // length
        acost = 1 if a <= length else (1 + a // length if a % length != 0 else a // length)
        result = min(result, lencost + bcost + acost)
        # print(length, acost + bcost + lencost)
    return result

for line in lines[1:]:
    a, b = map(int, line.split())
    print(solve(a, b))
    # print(result)
