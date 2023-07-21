import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from bisect import bisect_left
from functools import lru_cache

sys.setrecursionlimit(10**6)

import math
N = 10**5 + 100
# stores smallest prime factor for every number

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    n = len(nums)

    @lru_cache(maxsize=None)
    def recur(i, cl):
        if i == n:
            return 0
        a = 1 + recur(i+1, lcm(cl, nums[i])) if lcm(cl, nums[i]) <= n else 0
        b = recur(i+1, cl)
        return max(a, b)
    print(recur(0, 1))
    
        