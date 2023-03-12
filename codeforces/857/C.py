import sys
lines = list(map(str.strip, sys.stdin.readlines()))


a = [[9740, 1549, 9744, 1553, 9748],
 [1550, 1551, 1554, 1555, 1558],
 [10252, 2061, 10256, 2065, 10260],
 [2062, 2063, 2066, 2067, 2070]]

b = [[3108, 3109, 3112, 3113],
 [3110, 3111, 3114, 3115],
 [3620, 3621, 3624, 3625],
 [3622, 3623, 3626, 3627]]

c=  [[25800, 25801, 25804, 25805, 25808, 25809],
 [25802, 4294993099, 25806, 4294993103, 25810, 4294993107],
 [26312, 26313, 26316, 26317, 26320, 26321],
 [26314, 4294993611, 26318, 4294993615, 26322, 4294993619],
 [26824, 26825, 26828, 26829, 26832, 26833],
 [26826, 4294994123, 26830, 4294994127, 26834, 4294994131]]

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
    for i in range(n):
        for j in range(m):
            matrix[i][j] = (i << 10) + j
    print(n*m)
    for row in matrix:
        print(*row)
    # print(check_submatrices(matrix))

# print(check_submatrices(a))
# print(check_submatrices(b))
# print(check_submatrices(c))

