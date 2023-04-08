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
    copy = []
    for j in range(n):
        copy.append([0]*n)
        for k in range(n):
            copy[j][k] = matrix[j][k]
    for _ in range(2):
        rotateMatrix(copy)
    operations = 0
    for j in range(n):
        if operations > k: break
        for k in range(n):
            if matrix[j][k] != copy[j][k]:
                operations += 1
                if operations > k:
                    break
    print("YES" if k <= operations  else "NO")

    # for xs in matrix:
    #     print(xs)
    # print()
    # for xs in copy:
    #     print(xs)

    # print()
