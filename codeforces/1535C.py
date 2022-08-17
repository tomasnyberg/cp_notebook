import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from heapq import heappop, heappush

for line in lines[1:]:
    dp = [[0, 0] for i in range(len(line))]
    dp[0][0] = 1 if line[0] == '0' or line[0] == '?' else 0
    dp[0][1] = 1 if line[0] == '1' or line[0] == '?' else 0
    for i in range(1, len(line)):
        if line[i] != '1':
            dp[i][0] = 1 + dp[i-1][1]
        if line[i] != '0':
            dp[i][1] = 1 + dp[i-1][0]
    result = 0
    for i in range(len(dp)):
        result += max(dp[i][0], dp[i][1])
    print(result)
