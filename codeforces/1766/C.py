import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def dfs(matrix, i, j, visited, blacks):
    if matrix[i][j] != 'B':
        return False
    visited.add((i, j))
    while True:
        good = False
        for di, dj in [[1,0], [-1, 0], [0,1]]:
            if 0 <= i+di < len(matrix) and 0 <= j+dj < len(matrix[0]) and (i+di, j+dj) not in visited and matrix[i+di][j+dj] == 'B':
                good = True
                i += di
                j += dj
                break
        visited.add((i, j))
        if len(visited) == blacks:
            return True
        if not good: return False

for i in range(1, len(lines), 3):
    n = int(lines[i])
    matrix = [lines[i+1], lines[i+2]]
    blacks = 0
    for row in matrix:
        for c in row:
            if c == 'B':
                blacks += 1
    a = dfs(matrix, 0, 0, set(), blacks)
    b = dfs(matrix, 1, 0, set(), blacks)
    print("YES" if a or b else "NO")



    
    