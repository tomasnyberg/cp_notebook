import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict
def cumsum2d(arr):
    result = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr[0])):
            sum += arr[i][j]
            result[i][j] = sum + (result[i-1][j] if i > 0 else 0)
    return result

# How you actually query the 2d prefix array
def query(cs2d, a, b, A, B): # a, b are the coordinates of the top left corner, A, B are the coordinates of the bottom right corner
    result = 0
    result += cs2d[A][B]
    result += cs2d[a-1][b-1] if a-1 >= 0 and b-1 >= 0 else 0
    result -= cs2d[a-1][B] if a-1 >= 0 else 0
    result -= cs2d[A][b-1] if b-1 >= 0 else 0
    return result

ii = 1
while ii < len(lines):
    n, m, k = map(int, lines[ii].split())
    ii+=1
    matrix = []
    for _ in range(n):
        curr = (list(map(lambda x: 1 if x == '#' else 0, lines[ii])))
        matrix.append([0]*m + curr + [0]*m)
        ii+=1
    for _ in range(n):
        matrix.append([0]*(3*m))
    matrix.reverse()
    for _ in range(n):
        matrix.append([0]*(3*m))
    matrix.reverse()
    csmatrix = cumsum2d(matrix)
    combs = [(1,1), (1,-1), (-1,1), (-1,-1)]
    for xs in matrix:
        print(xs)
    def score(i, j, vert_dir, diagdir, k):
        if k == 0 or i < 0 or i >= len(matrix) or j < 0 or j > len(matrix[0]):
            return 0
        if k == 1:
            return matrix[i][j]
        capi = i + k*vert_dir
        capj = j + k*diagdir
        square = (k+1)//2
        points = [(i, j), (i+square*vert_dir, j+square*diagdir), (i+square*vert_dir, j), (i, j+square*diagdir)]
        points.sort()
        a,b = points[0]
        A,B = points[3]
        scorethis = query(csmatrix, a,b,A,B)
        vert_score = score(i+square*vert_dir, j, vert_dir, diagdir, k - square)
        diag_score = score(i, j+square*diagdir, vert_dir, diagdir, k - square)
        return scorethis + vert_score + diag_score
    result = 0
    seenmatrix = []
    for i in range(n, 2*n):
        curr = []
        for j in range(m, 2*m):
            curr.append(matrix[i][j])
            for vert_dir, diagdir in combs:
                result = max(result, score(i, j, vert_dir, diagdir, k))
        seenmatrix.append(curr)
    print("Seen matrix")
    for xs in seenmatrix:
        print(xs)
    print(result)