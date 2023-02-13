import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache

n, x = map(int, lines[0].split())

@lru_cache(None)
def brute_force(x):
    s = str(x)
    if len(s) == n:
        return 0
    fastest = 10**9
    for c in s:
        if int(c) > 1:
            res = 1 + brute_force(x*int(c))
            if res == 0: continue
            fastest = min(fastest, res)
    return fastest if fastest != 10**9 else -1

print(brute_force(x))
    