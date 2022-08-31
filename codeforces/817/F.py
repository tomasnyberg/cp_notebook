import sys
lines = list(map(str.strip, sys.stdin.readlines()))
sys.setrecursionlimit(2501)
 
i = 1
while i < len(lines):
    n, m = map(int, lines[i].split(" "))
    matrix = []
    i+=1
    while n > 0:
        matrix.append(list(lines[i]))
        n-=1
        i+=1
    # All 8 directions in a 2d matrix
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
    def dfs(r, c, matrix, visited):
        # print("at", r, c)
        visited.append((r, c))
        matrix[r][c] = '.'
        for dr, dc in directions:
            newr = r + dr
            newc = c + dc
            if newr >= 0 and newr < len(matrix) and newc >= 0 and newc < len(matrix[0]) and matrix[newr][newc] == '*':
                dfs(r + dr, c + dc, matrix, visited)
    bad = False
    good = set([((0,0), (0,1), (1,1)), ((0,0), (1,0), (1,1)), ((0,0), (0,1), (1,0)), ((0,1), (1,0), (1,1))])
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == '.': continue
            visited = []
            dfs(r,c,matrix, visited)
            if len(visited) != 3:
                bad = True
                break
            # Sort visited primarily by the first key, secondarily by the second
            visited.sort(key = lambda x: (x[0], x[1]))
            smallestrow = min(visited, key = lambda x: x[0])[0]
            smallestcol = min(visited, key = lambda x: x[1])[1]
            visited = list(map(lambda x: (x[0] - smallestrow, x[1] - smallestcol), visited))
            if tuple(visited) not in good:
                bad = True
                break
    print("NO" if bad else "YES")
