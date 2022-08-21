import sys
lines = list(map(str.strip, sys.stdin.readlines()))

ptr = 1
while ptr < len(lines):
    n, m, k = map(int, lines[ptr].split(" "))
    ptr+=1
    grid = []
    for i in range(n):
        grid.append(list(map(lambda x: 1 if x == '*' else 0, lines[ptr])))
        ptr +=1
    found = 0
    total = sum([sum(xs) for xs in grid])
    # Mark a grid point with -1 if it has been found but should still count as a square
    # Go from bottom to top in the array
    for i in range(n-1, -1, -1):
        for j in range(m):
            if not grid[i][j]: continue
            if j >= k and m - 1 - j >= k: # If we have enough space to the left and to the right
                row = i-1
                goodrows = 1
                while True:
                    right = j + goodrows
                    left = j - goodrows
                    if right == m or left < 0 or not grid[row][left] or not grid[row][right]: break
                    row -=1 
                    goodrows+=1
                goodrows -=1
                if goodrows >= k:
                    print("found tick at", i, j)
                    if grid[i][j] == 1:
                        found +=1
                        grid[i][j] = -1
                    row = i-1
                    for l in range(1, goodrows+1):
                        right = j + l
                        left = j - l
                        if grid[row][right] == 1:
                            found += 1
                            grid[row][right] = -1
                        if grid[row][left] == 1:
                            found += 1
                            grid[row][left] = -1
                        row -= 1
    for xs in grid:
        print(xs)
    print("YES" if found == total else "NO")
