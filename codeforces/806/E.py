import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def rotateMatrix(matrix):
    n = len(matrix)
    for x in range(0, int(n / 2)):
        for y in range(x, n-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = temp

def solve(grid):
    result = 0
    counter = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    for _ in range(4):
        for i in range(len(grid)):
            for j in range(len(grid)):
                counter[i][j] += grid[i][j]
        rotateMatrix(grid)
    for i in range(len(grid) // 2):
        for j in range(i, len(grid) - i - 1):
            x = counter[i][j]
            result += min(4 - x, x)
    print(result)

i = 1
while i < len(lines):
    n = int(lines[i])
    grid = []
    i+=1
    while n > 0:
        grid.append(list(map(int, lines[i])))
        n-=1
        i+=1
    solve(grid)