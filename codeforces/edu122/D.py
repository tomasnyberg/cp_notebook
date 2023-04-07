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

def count_bits(n):
    big = 0
    for i in range(30):
        if n & (1 << i):
            big = i
    return big + bin(n).count('1') - 1

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
    b = list(map(lambda x: minimal_amount(x, 1), b))
    coins = list(map(int, lines[i + 2].split()))
    removed = set()
    result = 0
    for j in range(len(b)):
        if b[j] == 0:
            result += coins[j]
            removed.add(j)
    b = [b[j] for j in range(len(b)) if j not in removed]
    coins = [coins[j] for j in range(len(coins)) if j not in removed]
    ans, dp = knapsack(coins, b, k)
    print(ans + result)