def rotateMatrix(matrix):
    n = len(matrix)
    for x in range(0, int(n / 2)):
        for y in range(x, n-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = temp

def print_matrix(xss):
    for xs in xss:
        print(xs)

xss =  [[1,2,3],
        [4,5,6],
        [7,8,9]]
print_matrix(xss)
print()
rotateMatrix(xss)
print_matrix(xss)