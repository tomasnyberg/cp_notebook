import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def find_bad_cols(grid):
    bad_cols = set()
    for j in range(len(grid)):
        for k in range(m - 1):
            if grid[j][k] > grid[j][k+1]:
                otherindex = k + 1
                elem = grid[j][k+1]
                while otherindex < len(grid[j]) - 1 and grid[j][otherindex + 1] == elem:
                    otherindex += 1
                bad_cols.add(k)
                bad_cols.add(otherindex)
    return bad_cols

def swap_cols_in_grid(grid, a, b):
    result = []
    for row in grid:
        result.append(row.copy())
    for i in range(len(grid)):
        temp = result[i][a]
        result[i][a] = result[i][b]
        result[i][b] = temp 
    return result

def solve(bad_columns, grid):
    for x in bad_columns:
        for y in bad_columns:
            if x != y:
                swapped = swap_cols_in_grid(grid, x, y)
                if len(find_bad_cols(swapped)) == 0:
                    print(x+1, y+1)
                    return
    print(-1)


i = 1
while i < len(lines):
    n, m = map(int, lines[i].split(" "))
    i+=1
    grid = []
    while n > 0:
       grid.append(list(map(int, lines[i].split(" ")))) 
       n-=1
       i+=1
    if m == 1: # If the length of the columns are just one, we can simply change it into itself
        print(1, 1)
        continue
    bad_columns = find_bad_cols(grid)
    if len(bad_columns) == 0:
        print(1, 1)
        continue
    for xs in grid:
        print(xs)
    print(bad_columns)
    print()
    if len(bad_columns) > 4:
        print(-1)
        continue
    solve(bad_columns, grid)
    