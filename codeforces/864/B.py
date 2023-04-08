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

i = 1
while i < len(lines):
    n, k = map(int, lines[i].split())
    i+=1
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, lines[i].split())))
        i+=1
    dots = 0
    for xs in matrix:
        dots += sum(xs)
    if k >= dots and k % 2 == dots % 2:
        print("YES")
        continue
    for j in range(n):
        for jj in range(n):
            if matrix[j][jj] != matrix[n - j - 1][n - jj - 1]:
                k -= 1
                matrix[j][jj] = 0
                matrix[n - j - 1][n - jj - 1] = 0
    if k < 0 or k % 2 != 0:
        print("NO")
    else:
        print("YES")
