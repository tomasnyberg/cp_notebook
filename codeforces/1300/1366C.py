import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache
from collections import deque

ii = 1
while ii < len(lines):
    n, m = map(int, lines[ii].split())
    ii += 1
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, lines[ii].split())))
        ii += 1
    result = 0
    for d in range((n+m)):
        if 2*d == n+m-2:
            continue
        count = [0, 0]
        for j in range(d + 1):
            i = d - j
            if i >= n or j >= m:
                continue
            count[matrix[i][j]] += 1
            if n-1-i != i or m-1-j != j:
                count[matrix[n-1-i][m-1-j]] += 1
        change_to = 0 if count[0] > count[1] else 1
        for j in range(d + 1):
            i = d - j
            if i >= n or j >= m:
                continue
            if matrix[i][j] != change_to:
                result += 1
                matrix[i][j] = change_to
            if matrix[n-1-i][m-1-j] != change_to:
                result += 1
                matrix[n-1-i][m-1-j] = change_to
    print(result)
        
        


