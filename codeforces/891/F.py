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
        if x not in d:
            d[x] = Wrapper(0)
        d[x] += 1
    for _ in range(q):
        l, r = map(int, lines[i].split())
        queries.append((l, r))
        i+=1
    res = []
    for x, y in queries:
        count = 0
        # Calculate discriminant for quadratic equation
        discriminant = x**2 - 4*y
        # If discriminant is negative, no real roots
        if discriminant < 0:
            print(0, end=' ')
            continue
        
        # Calculate the two potential values of a
        a1 = (x + math.sqrt(discriminant)) / 2
        a2 = (x - math.sqrt(discriminant)) / 2
        
        # Check if both a1 and x-a1 exist in the array and aren't the same number (unless their frequency > 1)
        if a1 in d and (x - a1) in d:
            if a1 == (x - a1) and d[a1] > 1:
                count += (d[a1] * (d[a1] - 1)) // 2
            elif a1 != (x - a1):
                count += d[a1] * d[x - a1]

        # Check if both a2 and x-a2 exist in the array and aren't the same number (unless their duency > 1)
        if a2 in d and (x - a2) in d:
            if a2 == (x - a2) and d[a2] > 1:
                count += (d[a2] * (d[a2] - 1)) // 2
            elif a2 != (x - a2):
                count += d[a2] * d[x - a2]
        print(count // 2, end= ' ')
    print()


