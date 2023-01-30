import sys
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

def comp(a, b):
    if a < b: return -1
    if a > b: return 1
    return 0

for line in lines[1:]:
    n = len(line)
    s = line
    dp = [[0 for _ in range(n+5)] for _ in range(n+5)]
    for length in range(2, n+1, 2):
        for l in range(n-length+1):
            r = l + length
            dp[l][r] = 1
            res = -1
            if dp[l+1][r-1] != 0:
                res = max(res, dp[l+1][r-1])
            else:
                res = max(res, comp(s[l], s[r-1]))
            if dp[l+2][r] != 0:
                res = max(res, dp[l+2][r])
            else:
                res = max(res, comp(s[l], s[l+1]))
            dp[l][r] = min(dp[l][r], res)
            res = -1
            if dp[l+1][r-1] != 0:
                res = max(res, dp[l+1][r-1])
            else:
                res = max(res, comp(s[r-1], s[l]))
            if dp[l][r-2] != 0:
                res = max(res, dp[l][r-2])
            else:
                res = max(res, comp(s[r-1], s[r-2]))
            dp[l][r] = min(dp[l][r], res)
    print("Alice" if dp[0][n] == -1 else "Draw")