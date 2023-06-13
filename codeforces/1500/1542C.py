import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import random

mod = 10**9 + 7

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

for line in lines[1:]:
    n = int(line)
    G = 1
    i = 1
    result = 0
    while G <= n:
        G = lcm(G, i)
        if G > n: break
        result += n // G
        i += 1
    print((result + n) % mod)
