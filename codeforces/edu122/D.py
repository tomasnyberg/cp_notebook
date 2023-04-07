import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))

# a = 1
# for i in range(15):
#     a += a // 1
#     print(i, a)

def count_bits(n):
    res = 0
    while n > 0:
        res += n % 2
        n //= 2
    return res

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
    print(b)
    b = list(map(count_bits, b))
    print(b)
    coins = list(map(int, lines[i + 2].split()))
    print(coins)
    ans, dp = knapsack(coins, b, k)
    print(ans)