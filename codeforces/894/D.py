import sys
from math import sqrt
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict
def nCr(n,r):
    import math
    return math.factorial(n) // (math.factorial(r)*(math.factorial(n-r)))

def solve_n(y):
    return (-1 + sqrt(1 + 8*y))/2

def f(x):
    if mid == 1:
        return 0
    return (x*(x+1))//2

def check(target, mid):
    return f(mid) <= target

for line in lines[1:]:
    x = int(line)
    low = 0
    high = 10**20
    while low < high:
        mid = (low + high) >> 1
        if check(x, mid):
            low = mid + 1
        else:
            high = mid
    if f(mid) > x:
        mid -= 1
    if mid == 1:
        mid -=1
    print(mid + x - f(mid) + 1)