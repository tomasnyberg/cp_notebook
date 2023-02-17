import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    matrix = [lines[i+1], lines[i+2]]
    for _ in range(2):
        while matrix[0][-1] == '.' and matrix[1][-1] == '.':
            matrix[0] = matrix[0][:-1]
            matrix[1] = matrix[1][:-1]
        matrix[0] = matrix[0][::-1]
        matrix[1] = matrix[1][::-1]
    dp = [[10**9 for _ in range(len(matrix[0]))] for _ in range(2)]
    for i in range(2):
        dp[i][0] = 1 if matrix[1-i][0] == '*' else 0
    for c in range(1,len(matrix[0])):
        for r in range(2):
            a = (dp[r][c-1] if c-1 >= 0 else 0) + 1 + (1 if matrix[r-1][c] == '*' else 0)
            b = (dp[r-1][c-1] if c -1 >= 0 else 0) + 2 # Come here from the element diagonally back
            dp[r][c] = min(a, b)
    results = {}
    # for xs in dp:
    #     print(xs)
    print(min(dp[0][-1], dp[1][-1]))




