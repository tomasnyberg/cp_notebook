import sys
lines = list(map(str.strip, sys.stdin.readlines()))

ii = 1
while ii < len(lines):
    grid = []
    for _ in range(8):
        grid.append(lines[ii])
        ii += 1
    word = ""
    for r in range(8):
        for c in range(8):
            if grid[r][c] != ".":
                word += grid[r][c]
    print(word)