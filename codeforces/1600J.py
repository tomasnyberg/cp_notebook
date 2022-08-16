import sys, threading
lines = list(map(str.strip, sys.stdin.readlines()))
 
n, m = map(int, lines[0].split(" "))
matrix = []
for i in range(1, len(lines)):
    matrix.append(list(map(int, lines[i].split(" "))))
dirs = [[0,-1], [1, 0], [0,1], [-1, 0]]
# for xs in matrix:
#     for x in xs:
#         binary = bin(x)[2:]
#         binary = "0"*(4-len(binary)) + binary
#         print(binary, end=" ")
#     print()

def inbounds(i, j):
    return i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[0]) and matrix[i][j] != -1
def dfs(i, j):
    # print("dfs at", i, j)
    original = matrix[i][j]
    matrix[i][j] = -1
    size = 1
    for k in range(len(dirs)):
        ni = i + dirs[k][0]
        nj = j + dirs[k][1]
        if inbounds(ni, nj) and original & (1 << k) == 0:
            size += dfs(ni, nj)
    return size
rooms = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] != -1:
            rooms.append(dfs(i, j))
rooms.sort(key=lambda x: -x)
for room in rooms:
    print(room, end=" ")
print()
