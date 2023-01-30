import sys
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

for line in lines[1:]:
    s = line
    while (s and s[0] == s[-1]): s = s[1:-1]
    res = "Draw"
    for i in range(0, len(s), 2):
        if s[i] != s[i+1]:
            res = "Alice"
            break
    print(res)