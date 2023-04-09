import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    low = 1
    matrix = [[0 for _ in range(n)] for _ in range(2)]
    matrix[0][0] = 2*n
    matrix[1][n-1] = 2*n - 1
    high = 2*n // 2 + 1
    up = 0
    for i in range(n):
        if i != 0 and i != n-1:
            matrix[up][i] = high
            high += 1
        matrix[1-up][i] = low
        low += 1
        up = 1-up
    # for i in range(1, n-1):
    #     # if i % 2 == 1:
    #     matrix[1][i], matrix[0][i+1] = matrix[0][i+1], matrix[1][i]
        # else:
        #     matrix[0][i], matrix[1][i+1] = matrix[1][i+1], matrix[0][i]
    for row in matrix:
        print(*row)