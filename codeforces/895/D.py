import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

import math
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

def f(x):
    return x*(x+1)//2

for line in lines[1:]:
    n, x, y = map(int, line.split())
    common = n // math.lcm(x, y)
    xs = n // x - common
    ys = n // y - common
    score = f(n) - f(n-xs)
    score -= f(ys)
    print(score)


