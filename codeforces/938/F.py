import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache
# TODO Remember to add int wrapping if using dict

@lru_cache(None)
def recur(one, two, three):
    if one == 0 and two == 0 and three == 0:
        return 0
    zeroth = one + three
    first = two + three
    add = 1 if zeroth % 2 == 0 and first % 2 == 0 else 0
    result = add
    if one > 0:
        result = max(result, add + recur(one - 1, two, three))
    if two > 0:
        result = max(result, add + recur(one, two - 1, three))
    if three > 0:
        result = max(result, add + recur(one, two, three - 1))
    return result

dp = [[[0 for _ in range(200 + 1)] for _ in range(200 + 1)] for _ in range(200 + 1)]
for i in range(200 + 1):
    for j in range(200 + 1):
        for k in range(200 + 1):
            if i == 0 and j == 0 and k == 0:
                continue
            zeroth = i + k
            second = j + k
            add = 1 if zeroth % 2 == 0 and second % 2 == 0 else 0
            result = add
            if i > 0:
                result = max(result, add + dp[i - 1][j][k])
            if j > 0:
                result = max(result, add + dp[i][j - 1][k])
            if k > 0:
                result = max(result, add + dp[i][j][k - 1])
            dp[i][j][k] = result
for line in lines[1:]:
    a, b, c, d = map(int, line.split())
    print(dp[a][b][c] + d // 2)
    # print(dp[a][b][c] + d // 2)

        
