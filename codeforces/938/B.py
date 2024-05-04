import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import Counter
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, c, d = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    # print(nums)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    counts = dict(Counter(nums))
    matrix[0][0] = min(nums)
    for i in range(1,n):
        matrix[i][0] = matrix[i-1][0] + c
    result = True
    for i in range(n):
        for j in range(1, n):
            matrix[i][j] = matrix[i][j-1] + d
    for i in range(n):
        for j in range(n):
            if matrix[i][j] not in counts:
                result = False
                break
            counts[matrix[i][j]] -= 1
            if counts[matrix[i][j]] == 0:
                del counts[matrix[i][j]]
    nums.sort()
    # print(nums)
    # for xs in matrix:
    #     print(xs)
    result = result and len(counts) == 0
    print("YES" if result else "NO")