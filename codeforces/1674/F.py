import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def print_grid(grid):
    for xs in reversed(grid):
        print(xs)

def count_stars(grid):
    result = 0
    for row in grid:
        for x in row:
            if x == 1:
                result +=1
    return result

def find_holes(grid, rtsbf, ctsbf):
    holes = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0 and (i < rtsbf or (i == rtsbf and j< ctsbf)):
                holes.add(str(i) + " " + str(j))
    return holes

a = 0
while a < len(lines):
    n, m, q = map(int, lines[a].split(" "))
    grid = []
    a +=1
    while n > 0:
        grid.append(list(map(lambda x: 1 if x == '*' else 0, lines[a])))
        n-= 1
        a+=1
    queries = []
    while q > 0:
        queries.append(list(map(int, lines[a].split(" "))))
        a+=1
        q-=1
    grid.reverse()
    starcount = count_stars(grid)
    rtsbf = starcount // m # Amount of rows that shuold be filled
    ctsbf = starcount % m # Amount of colummns that shuold be filled
    holes = find_holes(grid, rtsbf, ctsbf)
    print("initial state, starcount", starcount)
    print_grid(grid)
    print()
    for i, j in queries:
        i -= 1
        j -= 1
        starcount += 1 if grid[i][j] == 0 else -1 # add star or remove star from count
        rtsbf = starcount // m # Amount of rows that shuold be filled
        ctsbf = starcount % m # Amount of colummns that shuold be filled
        if ctsbf > 0:
            ctsbf -=1
        else:
            rtsbf -=1
            ctsbf = m - 1
        coord = str(i) + " " + str(j)
        grid[i][j] = 0 if grid[i][j] == 1 else 1 # toggle
        if grid[i][j] == 1 and coord in holes: # If we had a hole at the (now) filled location
            holes.remove(coord)
        if grid[i][j] == 0 and (i < rtsbf or (i == rtsbf and j< ctsbf)): # The second boolean might be wrong
            holes.add(coord)
        if grid[rtsbf][ctsbf] != 1:
            holes.add(str(rtsbf) + " " + str(ctsbf))
        print("flipped", i, j)
        print("starcount", starcount)
        print_grid(grid)
        print("rtsbf", rtsbf, "ctsbf", ctsbf)
        print(holes)
        print(len(holes))
        print() 