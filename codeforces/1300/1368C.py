import sys
lines = list(map(str.strip, sys.stdin.readlines()))

n = int(lines[0])
grid = [[0] * (3*n + 5) for _ in range(3*n + 5)]
i = 0
j = 0
for _ in range(n + 1):
    for k in range(3):
        for l in range(3):
            grid[i+k][j+l] = 1
    grid[i+1][j+1] = 0
    i += 2
    j += 2
print(sum([sum(row) for row in grid]))
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j]:
            print(i+1, j+1)
