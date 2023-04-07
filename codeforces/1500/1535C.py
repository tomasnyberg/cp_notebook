import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    dp = [[0, 0] for i in range(len(line))]
    for i in range(len(line)):
        if line[i] != '1':
            dp[i][0] = 1 + (dp[i-1][1] if i > 0 else 0)
        if line[i] != '0':
            dp[i][1] = 1 + (dp[i-1][0] if i > 0 else 0)
    result = 0
    for i in range(len(dp)):
        result += max(dp[i][0], dp[i][1])
    print(result)
