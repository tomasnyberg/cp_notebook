import sys
lines = list(map(str.strip, sys.stdin.readlines()))

x = 2*10**3 
dp = [10**9] * (x + 1)
dp[1] = 0

for i in range(1, x + 1):
    dp[i] = min(dp[i], 1 + dp[i - 1])
    for j in range(1, i + 1):
        if i + i//j >= len(dp): break
        dp[i + (i//j)] = min(dp[i] + 1, dp[i + (i//j)])

def knapsack(values, weights, capacity):
    dp = [[0] * (capacity + 1) for _ in range(2)]
    for i in range(1, len(values) + 1):
        for j in range(1, capacity + 1):
            dp[i % 2][j] = dp[(i - 1) % 2][j]
            if weights[i - 1] <= j:
                dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - weights[i - 1]] + values[i - 1])
    return dp[len(values) % 2][-1]


for i in range(1, len(lines), 3):
    n, k = map(int, lines[i].split())
    b = list(map(int, lines[i + 1].split()))
    b = list(map(lambda x: dp[x], b))
    k = min(k, sum(b))
    coins = list(map(int, lines[i + 2].split()))
    removed = set()
    result = 0
    for j in range(len(b)):
        if b[j] == 0:
            result += coins[j]
            removed.add(j)
    b = [b[j] for j in range(len(b)) if j not in removed]
    coins = [coins[j] for j in range(len(coins)) if j not in removed]
    ans = knapsack(coins, b, k)
    print(ans + result)