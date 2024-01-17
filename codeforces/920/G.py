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

# lines ="""4
# 2 1 3
# #
# #
# """.splitlines()

ii = 1
while ii < len(lines):
    n, m, k = map(int, lines[ii].split())
    ii+=1
    matrix = []
    for _ in range(n):
        curr = (list(map(lambda x: 1 if x == '#' else 0, lines[ii])))
        matrix.append([0]*(2*m) + curr + [0]*(2*m))
        ii+=1
    for _ in range(2*n):
        matrix.append([0]*(5*m))
    matrix.reverse()
    for _ in range(2*n):
        matrix.append([0]*(5*m))
    matrix.reverse()
    csmatrix = cumsum2d(matrix)
    combs = [(1,1), (1,-1), (-1,1), (-1,-1)]
    k = min(k, max(n,m)*2)
    count = [0]
    def score(i, j, vert_dir, diagdir, k):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
            return 0
        if i < 2*n or i >= 3*n or j < 2*m or j >= 3*m:
            return 0
        if k == 0:
            return matrix[i][j]
        count[0] += 1
        square = (k+2)//2
        
        # print("k and square", k, square)
        points = [[i, j], [i+(square-1)*vert_dir, j+(square-1)*diagdir], [i+(square-1)*vert_dir, j], [i, j+(square-1)*diagdir]]
        for xs in points:
            xs[0] = max(xs[0], 0)
            xs[0] = min(xs[0], len(matrix)-1)
            xs[1] = max(xs[1], 0)
            xs[1] = min(xs[1], len(matrix[0])-1)
        # print(points)
        points.sort()
        a,b = points[0]
        A,B = points[3]
        scorethis = query(csmatrix, a,b,A,B)
        vert_score = score(i+(square)*vert_dir, j, vert_dir, diagdir, k - square)
        diag_score = score(i, j+(square)*diagdir, vert_dir, diagdir, k - square)
        return scorethis + vert_score + diag_score
    result = 0
    seenmatrix = []
    # for xs in matrix:
    #     print(xs)
    for i in range(2*n, 3*n):
        curr = []
        for j in range(2*m, 3*m):
            curr.append(matrix[i][j])
            for vert_dir, diagdir in combs:
                sc = score(i, j, vert_dir, diagdir, k)
                # print("count", count[0])
                count[0] = 0
                # print(i, j, sc)
                result = max(result, sc)
        seenmatrix.append(curr)
    # print("Seen matrix")
    # for xs in seenmatrix:
    #     print(xs)
    print(result)