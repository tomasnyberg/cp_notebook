import sys
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    s = list(line)
    if all(c == 'A' for c in s):
        print(0)
        continue
    result = 0
    # print(''.join(s))
    indices = [i for i in range(len(s)) if s[i] == 'B']
    def iterative_dp(indices, s):
        n = len(indices)
        # dp[i][j] represents the maximum value when considering the first i elements of indices
        # and j indicates whether the previous element was taken (j=0 means not taken, j=1 means taken)
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for prev_taken in [True, False]:
                j = 1 if prev_taken else 0
                if prev_taken:
                    if i == n - 1:
                        dp[i][j] = len(s) - indices[i] - 1
                    else:
                        dp[i][j] = indices[i + 1] - indices[i] - 1 + dp[i + 1][1]
                else:
                    previous = indices[i - 1] if i > 0 else -1
                    take_previous = indices[i] - previous - 1 + dp[i + 1][0]
                    take_next = (len(s) - indices[i] if i == n - 1 else indices[i + 1] - indices[i]) - 1 + dp[i + 1][1]
                    dp[i][j] = max(take_previous, take_next)

        return dp[0][0]

    print(iterative_dp(indices, s))
