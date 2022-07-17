import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def print_grid(grid):
    for xs in grid:
        print(xs)

i = 0
while i < len(lines):
    n, m, q = map(int, lines[i].split(" "))
    grid = []
    i +=1
    while n > 0:
        grid.append(lines[i])
        n-= 1
        i+=1
    queries = []
    while q > 0:
        queries.append(list(map(int, lines[i].split(" "))))
        i+=1
        q-=1
    starcount = 0
    for row in grid:
        for x in row:
            if x == '*':
                starcount +=1
    rtsbf = starcount // m # Amount of rows that shuold be filled
    ctsbf = starcount % m # Amount of colummns that shuold be filled
    print(rtsbf)
    print(ctsbf)
    holes = []
    for i in range(n):
        for j in range(m):
            if i+1 < rtsbf or (i+1 == rtsbf and j+1 <= ctsbf):
                holes.append([i, j])
    print(holes)
