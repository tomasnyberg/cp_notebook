import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def count_subsequences(a, n, target):
    MOD = 10**9 + 7
    big = max(a)
    dp = [[0] * (big + 1) for _ in range(n + 1)]
    # dp[0][0] = 1
    for i in range(1, n+1):
        curr = a[i-1]
        for k in range(0, big + 1):
            dp[i][k] += dp[i-1][k]
            dp[i][k & curr] += dp[i-1][k]
            dp[i][k & curr] %= MOD
        dp[i][curr] += 1
    result = 0
    # for xs in dp:
    #     print(xs)
    for i in range(big + 1):
        if bin(i).count("1") == target:
            result += dp[n][i]
            result %= MOD
    return result


ii = 1
while ii < len(lines):
    n, k = map(int, lines[ii].split())
    ii+=1
    nums = list(map(int, lines[ii].split()))
    ii+=1
    print(count_subsequences(nums, n, k))