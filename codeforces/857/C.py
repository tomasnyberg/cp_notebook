import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check_submatrices(B):
    rows, cols = len(B), len(B[0])
    for i in range(rows-3):
        for j in range(cols-3):
            A11, A12, A13, A14 = B[i][j], B[i][j+1], B[i][j+2], B[i][j+3]
            A21, A22, A23, A24 = B[i+1][j], B[i+1][j+1], B[i+1][j+2], B[i+1][j+3]
            A31, A32, A33, A34 = B[i+2][j], B[i+2][j+1], B[i+2][j+2], B[i+2][j+3]
            A41, A42, A43, A44 = B[i+3][j], B[i+3][j+1], B[i+3][j+2], B[i+3][j+3]
            if A11^A12^A21^A22 != A33^A34^A43^A44 or A13^A14^A23^A24 != A31^A32^A41^A42:
                return False
    return True

for line in lines[1:]:
    n, m = map(int, line.split())
    matrix = [[0] * m for _ in range(n)]
    for i in range(0, n, 2):
        for j in range(0, m, 2):
            for idx, (di, dj) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1)]):
                if i+di < n and j+dj < m:
                    matrix[i+di][j+dj] = idx
    for i in range(n):
        for j in range(m):
            matrix[i][j] |= (i << 3) | (j << 20) 
    print(n*m)
    for xs in matrix:
        print(*xs)
    # print(check_submatrices(matrix))
