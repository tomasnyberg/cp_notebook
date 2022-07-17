import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def print_grid(grid, cols):
    for i in range(len(grid)):
        if i % cols == 0 and i != 0:
            print()
        print(grid[i], end="")
    print()

def solve(grid, stars):
    result = 0
    for i in range(stars):
        if grid[i] == 0:
            result += 1
    return result


i = 0
while i < len(lines):
    n, m, q = map(int, lines[i].split(" "))
    rows = n
    cols = m
    grid = []
    i +=1
    while n > 0:
        grid += list(map(lambda x: 1 if x == '*' else 0, lines[i]))
        n-= 1
        i+=1
    queries = []
    while q > 0:
        queries.append(list(map(int, lines[i].split(" "))))
        i+=1
        q-=1
    totalstars = sum(grid)
    for r, c in queries:
        idx = (r-1)*cols + (c-1)
        grid[idx] = 1 if grid[idx] == 0 else 0
        totalstars += 1 if grid[idx] == 1 else -1
        print_grid(grid, cols)
        print(solve(grid, totalstars))