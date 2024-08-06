import sys
from collections import deque
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, m = map(int, lines[ii].split())
    nums = list(map(int, lines[ii + 1].split()))
    trailing0s = []
    for x in nums:
        orig = x
        count = 0
        while x % 10 == 0:
            x //= 10
            count += 1
        trailing0s.append([count, orig])
    trailing0s.sort(key=lambda x: x[0], reverse=True)
    for i, (x, orig) in enumerate(trailing0s):
        if i % 2 == 1:
            trailing0s[i][0] = 0
    totlen = 0
    for divisions, orig in trailing0s:
        while divisions > 0:
            orig //= 10
            divisions -= 1
        totlen += len(str(orig))
    print("Sasha" if totlen >= m + 1 else "Anna")
