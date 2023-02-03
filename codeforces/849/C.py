import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

for s in lines[2::2]:
    s = deque(s)
    while len(s) > 1:
        if s[0] != s[-1]:
            s.popleft()
            s.pop()
        else:
            break
    print(len(s))
     