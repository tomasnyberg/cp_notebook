import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

for line in lines[1:]:
    n, k = map(int, line.split())
    if n % 3 == 0:
        print(n // 3, n // 3, n // 3)
        continue
    if n % 2 == 1:
        print(1, (n-1) // 2, (n-1) // 2)
        continue
    if n % 2 == 0 :
        if (n // 2) % 2 == 0:
            print(n//2, n//4, n//4)
        else:
            print(2, (n-2) // 2, (n-2) // 2)

