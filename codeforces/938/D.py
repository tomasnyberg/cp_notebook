import sys
from collections import Counter
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict
from random import getrandbits

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


for ii in range(1, len(lines), 3):
    n, m, k = map(int, lines[ii].split())
    a = list(map(int, lines[ii+1].split()))
    b = list(map(int, lines[ii+2].split()))
    a = [Wrapper(x) for x in a]
    b = [Wrapper(x) for x in b]
    targets = dict(Counter(b))
    negative = 0
    left = 0
    right = 0
    result = 0
    while right < len(a):
        if a[right] in targets:
            targets[a[right]] -= 1
            if targets[a[right]] >= 0:
                negative += 1
        if right - left + 1 == m:
            result += 1 if negative >= k else 0
            if a[left] in targets:
                if targets[a[left]] >= 0:
                    negative -= 1
                targets[a[left]] += 1
            left += 1
        right += 1
    print(result)