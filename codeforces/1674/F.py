import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def print_grid(grid, cols):
    for i in range(len(grid)):
        if i % cols == 0 and i != 0:
            print()
        print(grid[i], end="")
    print()


i = 0
while i < len(lines):
    n, m, q = map(int, lines[i].split(" "))
    rows = n
    cols = m
    grid = []
    i +=1
    while n > 0:
        grid.append(list(map(lambda x: 1 if x == '*' else 0, lines[i])))
        n-= 1
        i+=1
    queries = []
    while q > 0:
        queries.append(list(map(int, lines[i].split(" "))))
        i+=1
        q-=1
    icons = []
    for c in range(cols):
        for r in range(rows):
            icons.append(grid[r][c])
    totalstars = sum(icons)
    for x, y in queries:
        p = rows*(y-1) + (x-1)
        icons[p] = 1 if icons[p] == 0 else 0
        totalstars += 1 if icons[p] == 1 else -1
        result = 0
        for k in range(totalstars):
            if icons[k] == 0:
                result +=1
        print(result)