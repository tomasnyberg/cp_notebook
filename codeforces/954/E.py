from random import getrandbits
import sys
from collections import defaultdict
from functools import lru_cache
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict


RANDOM = getrandbits(32)


class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)

    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


def get_sum(xs):
    result = 0
    for i in range(1, len(xs), 2):
        result += xs[i] - xs[i-1]
    return result


for ii in range(1, len(lines), 2):
    n, kk = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    nums = [Wrapper(x) for x in nums]
    mods = defaultdict(list)
    for x in nums:
        mods[Wrapper(x % kk)].append(x)
    can_be_removed = len(nums) % 2
    for k, v in list(mods.items()):
        v.sort()
        if len(v) % 2 == 1:
            can_be_removed -= 1
    if can_be_removed < 0:
        print(-1)
        continue
    result = 0
    for k, v in mods.items():
        if len(v) % 2 == 1:
            if len(v) == 1:
                continue

            n = len(v)
            dp = [[0]*(n+1) for _ in range(2)]
            dp[1][n-1] = 10**9

            for i in range(n-2, -1, -1):
                dp[0][i] = dp[0][i+2] + v[i+1] - v[i]
                dp[1][i] = min(dp[0][i+1], dp[1][i+2] + v[i+1] - v[i])

            result += min(dp[1][0], dp[0][0]) // kk
            continue

        for i in range(0, len(v), 2):
            result += (v[i+1] - v[i]) // kk
    # print(mods)
    print(result)
