import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

ii = 1
while ii < len(lines):
    n, m = map(int, lines[ii].split())
    ii += 1
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, lines[ii].split())))
        ii += 1
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(n):
        for j in range(m):
            greater_than_all = True
            biggest_nbr = 0
            for di, dj in dirs:
                oi, oj = i + di, j + dj
                if 0 <= oi < n and 0 <= oj < m:
                    biggest_nbr = max(biggest_nbr, matrix[oi][oj])
                    if matrix[i][j] <= matrix[oi][oj]:
                        greater_than_all = False
                        break
            if greater_than_all:
                matrix[i][j] = biggest_nbr
    for row in matrix:
        print(*row)
