# Example taken from this youtube video by William Fiset:
# https://www.youtube.com/watch?v=cJ21moQpofY

def knapsack(values, weights, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(values) + 1)]
    for i in range(1, len(values) + 1):
        for j in range(1, capacity + 1):
            dp[i][j] = dp[i - 1][j]
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
    return (dp[-1][-1], dp)

def find_items(dp):
    items = []
    i, j = len(dp) - 1, len(dp[0]) - 1
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            items.append(i-1)
            j -= weights[i - 1]
        i -= 1
    return items

values = [2,2,4,5,3]
weights = [3,1,3,4,2]
ans, dp = knapsack(values, weights, 7)
print("Chosen items (0 indexed):", find_items(dp))
print("Max possible value:", ans)

