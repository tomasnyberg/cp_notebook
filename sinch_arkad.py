import sys, random
from heapq import heappop, heappush
lines = list(map(str.strip, sys.stdin.readlines()))

# with open("in", "w") as f:
#     for i in range(10):
#         for i in range(25):
#             for j in range(25):
#                 f.write(str(random.randint(-100, 100)) + " ")
#             f.write("\n")
#         f.write("\n")

def cumsum2d(arr):
    result = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr[0])):
            sum += arr[i][j]
            result[i][j] = sum + (result[i-1][j] if i > 0 else 0)
    return result

def query(cs2d, a, b, A, B): # a, b are the coordinates of the top left corner, A, B are the coordinates of the bottom right corner
    result = 0
    result += cs2d[A][B]
    result += cs2d[a-1][b-1] if a-1 >= 0 and b-1 >= 0 else 0
    result -= cs2d[a-1][B] if a-1 >= 0 else 0
    result -= cs2d[A][b-1] if b-1 >= 0 else 0
    return result

def solve(matrix):
    for _ in range(5):
        cs2d = cumsum2d(matrix)
        candidates = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                for d in range(len(matrix)):
                    if i + d == len(matrix) or j + d == len(matrix): break
                    qresult = -query(cs2d, i, j, i+d, j+d)
                    candidates.append((qresult, (i,j,d)))
        best = max(candidates, key=lambda x: x[0])
        row, col, d = best[1]
        for i in range(row, row+d+1):
            for j in range(col, col+d+1):
                matrix[i][j] *= -1

i = 0
while i < len(lines):
    matrix = []
    while i < len(lines) and lines[i] != "":
        matrix.append(list(map(int, lines[i].split(" "))))
        i+=1
    i+=1
    total = 0
    for xs in matrix:
        total += sum(xs)
    print("Total sum of matrix is", total)
    solve(matrix)
    total = 0
    for xs in matrix:
        total += sum(xs)
    print("NEW total sum of matrix is", total)
    print()
    