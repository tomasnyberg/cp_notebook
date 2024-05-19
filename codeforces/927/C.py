import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 3):
    n, m = map(int, lines[ii].split())
    a = list(map(int, lines[ii + 1].split()))
    a = deque(a)
    seq = lines[ii+2]
    removals = []
    for c in seq:
        if c == 'L':
            removed = a.popleft()
        else:
            removed = a.pop()
        removals.append(removed)
    result = []
    prod = 1
    for x in removals[::-1]:
        prod *= x
        prod %= m
        result.append(prod)
    print(' '.join(map(str, result[::-1])))
