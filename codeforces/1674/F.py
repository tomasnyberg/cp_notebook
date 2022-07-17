import sys
lines = list(map(str.strip, sys.stdin.readlines()))

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
    prefixsum = sum(icons[:totalstars])
    for x, y in queries:
        p = rows*(y-1) + (x-1)
        totalstars += 1 if icons[p] == 0 else -1
        if icons[p] == 0: # We are putting in a new icon
            icons[p] = 1
            if p < totalstars - 1:
                prefixsum += 1
            if icons[totalstars - 1] == 1: # Might be an issue with adding twice?
                prefixsum += 1
        else:
            if icons[totalstars] == 1:
                prefixsum -= 1
            icons[p] = 0
            if p < totalstars:
                prefixsum -= 1
        print(totalstars - prefixsum)