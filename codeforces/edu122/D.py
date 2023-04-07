import sys
import math
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))

@lru_cache(None)
def minimal_amount(target, curr):
    if target < curr:
        return 10**9
    if target == curr:
        return 0
    result = 10**9
    for i in range(1, curr + 1):
        result = min(result, 1 + minimal_amount(target, curr + curr // i))
    return result

x = 2*10**3 
dp = [10**9] * (x + 1)
dp[1] = 0

for i in range(1, x + 1):
    dp[i] = min(dp[i], 1 + dp[i - 1])
    for j in range(1, i + 1):
        if i + i//j >= len(dp): break
        dp[i + (i//j)] = min(dp[i] + 1, dp[i + (i//j)])

# print(dp)

def count_bits(n):
    return dp[n]

# for i in range(1, 1000):
#     if i % 100 == 0:
#         print(i)
#     if count_bits(i) != minimal_amount(i, 1):
#         print(i, bin(i), count_bits(i), minimal_amount(i, 1))

def knapsack(values, weights, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(values) + 1)]
    for i in range(1, len(values) + 1):
        for j in range(1, capacity + 1):
            dp[i][j] = dp[i - 1][j]
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
    return (dp[-1][-1], dp)

for i in range(1, len(lines), 3):
    n, k = map(int, lines[i].split())
    b = list(map(int, lines[i + 1].split()))
    b = list(map(lambda x: dp[x], b))
    coins = list(map(int, lines[i + 2].split()))
    removed = set()
    result = 0
    for j in range(len(b)):
        if b[j] == 0:
            result += coins[j]
            removed.add(j)
    b = [b[j] for j in range(len(b)) if j not in removed]
    coins = [coins[j] for j in range(len(coins)) if j not in removed]
    ans, _ = knapsack(coins, b, k)
    print(ans + result)