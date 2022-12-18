import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def rotateMatrix(matrix):
    n = len(matrix)
    for x in range(0, int(n / 2)):
        for y in range(x, n-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = temp

def beautiful(matrix):
    if matrix[0][0] < matrix[0][1] and matrix[1][0] < matrix[1][1]:
        if matrix[0][0] < matrix[1][0] and matrix[0][1] < matrix[1][1]:
            return True
    return False

for i in range(1, len(lines), 2):
    matrix = []
    for j in range(2):
        matrix.append(list(map(int, lines[i+j].split())))
    good = False
    for j in range(5):
        if beautiful(matrix):
            good = True
            break
        rotateMatrix(matrix)
    if good:
        print("YES")
    else:
        print("NO")
