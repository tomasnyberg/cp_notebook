import sys
from collections import deque
lines = list(map(str.strip, sys.stdin.readlines()))

dirs2d = [(0,1), (0,-1), (1,0), (-1,0)]

ii = 1
while ii < len(lines):
    n, m = map(int, lines[ii].split(" "))
    ii+=1
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, lines[ii].split(" "))))
        ii+=1
    visited = set()
    def bfs(matrix, r, c):
        q = deque([(r, c)])
        score = 0
        while q:
            i, j = q.popleft()
            if (i,j) in visited or matrix[i][j] == 0: continue
            visited.add((i,j))
            score += matrix[i][j]
            for di, dj in dirs2d:
                oi, oj = i + di, j + dj
                if 0 <= oi < n and 0 <= oj < m:
                    q.append((oi, oj))
        return score
    result = 0
    for i in range(n):
        for j in range(m):
            if (i,j) not in visited:
                result = max(result, bfs(matrix, i, j))
    print(result)
