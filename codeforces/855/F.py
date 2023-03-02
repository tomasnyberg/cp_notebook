import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache

vals = []
for line in lines[1:]:
    cor, xor = 0, 0
    for c in line:
        cor |= 1 << (ord(c) - ord('a'))
        xor ^= 1 << (ord(c) - ord('a'))
    vals.append((cor, xor))
cnt = {}
ans = 0
for k in range(26):
    goal = ((1 << 26) -1)^ (1 << k)
    for cor, xor in vals:
        if cor & (1 << k): continue
        ans += cnt.get(xor ^ goal, 0)
        cnt[xor] = cnt.get(xor, 0) + 1	
    for cor, xor in vals:
        if cor & (1 << k): continue
        cnt[xor] = cnt.get(xor, 0) - 1
print(ans)