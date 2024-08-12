import sys
from collections import defaultdict
from functools import lru_cache
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict


def get_sum(xs):
    result = 0
    for i in range(1, len(xs), 2):
        result += xs[i] - xs[i-1]
    return result


for ii in range(1, len(lines), 2):
    n, kk = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    mods = defaultdict(list)
    for x in nums:
        mods[x % kk].append(x)
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
            # @lru_cache(None)
            # def dp(i, one_removed):
            #     if i == len(v):
            #         return 0
            #     if i == len(v) - 1 and one_removed:
            #         return 0
            #     if i == len(v) - 1:
            #         return 10**9
            #     if not one_removed:
            #         return dp(i+2, 0) + v[i+1] - v[i]
            #     return min(dp(i+1, 0), dp(i+2, 1) + v[i+1] - v[i])
            dp = [[0]*2 for _ in range(n+1)]
            dp[n-1][1] = 10**9
            for i in range(n-2, -1, -1):
                dp[i][0] = dp[i+2][0] + v[i+1] - v[i]
                dp[i][1] = min(dp[i+1][0], dp[i+2][1] + v[i+1] - v[i])
            # for xs in dp:
            #     print(xs)
            result += min(dp[0][1], dp[0][0]) // kk
            # result += dp(0, 1)// kk
            continue
        for i in range(0, len(v), 2):
            result += (v[i+1] - v[i]) // kk
    # print(mods)
    print(result)
