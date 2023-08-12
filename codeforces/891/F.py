import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import Counter
# TODO Remember to add int wrapping if using dict

from random import getrandbits

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

def potential_b_values(x, y):
        delta = x**2 - 4*y
        if delta < 0:  # No real solutions
            return []

        root_delta = delta**0.5
        b1 = (x + root_delta) / 2
        b2 = (x - root_delta) / 2

        return [b1 if int(b1) == b1 else 10**10, b2 if int(b2) == b2 else 10**10]

i = 1
while i < len(lines):
    n = int(lines[i])
    i+=1
    a = list(map(int, lines[i].split()))
    i+=1
    q = int(lines[i])
    i+=1
    queries = []
    d = {}
    for x in a:
        x = Wrapper(x)
        if x not in d:
            d[x] = 0
        d[x] += 1
    for _ in range(q):
        l, r = map(int, lines[i].split())
        queries.append((l, r))
        i+=1
    res = []
    for x, y in queries:
        count = 0
        discriminant = x**2 - 4*y
        if discriminant < 0:
            print(0, end=' ')
            continue

        sqrt_discriminant = int(math.sqrt(discriminant))
        
        # Check if it's a perfect square
        if sqrt_discriminant ** 2 == discriminant:
            # Calculate the two potential values of c without floating point division
            a1 = (x + sqrt_discriminant) // 2
            a2 = (x - sqrt_discriminant) // 2
            
            for c in [a1, a2]:
                c = Wrapper(c)
                complement = Wrapper(x - c)
                if c in d and complement in d:
                    if c == complement and d[c] > 1:
                        count += (d[c] * (d[c] - 1)) // 2
                    elif c != complement:
                        count += d[c] * d[complement]
        print(count // 2, end=' ')
    print()


