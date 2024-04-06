import sys
from functools import lru_cache
from collections import deque
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

ii = 1
while ii < len(lines):
    n, m = map(int, lines[ii].split())
    ii+=1
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, lines[ii].split())))
        ii+=1
    q = deque([(0,0)])
    visited = set()
    result = 10**9
    level = 0
    while q:
        for _ in range(len(q)):
            i,j = q.popleft()
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if j == m-2:
                npos = ((n-1) + level) % n
                if npos < i:
                    npos += n
                cur = level + min(npos-i, n - (npos-i))
                result = min(result, cur)
                break
            if not matrix[(i+2) % n][j] and not matrix[(i+1) % n][j]:
                q.append(((i+2) % n, j))
            if j+1 < len(matrix[0]) and not matrix[(i+1) % n][j+1]:
                q.append(((i+1) % n, j+1))
        level += 1
    print(result + 1 if result < 10**9 else -1)


        