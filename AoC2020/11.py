import sys
lines = list(map(str.strip, sys.stdin.readlines()))

matrix = []
for line in lines:
    matrix.append(list(line))

dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

def occupied_near(m, i, j):
    result = 0
    for di, dj in dirs:
        ni = i + di
        nj = j + dj
        if 0 <= ni < len(m) and 0 <= nj < len(m[0]):
            if m[ni][nj] == '#':
                result += 1
    return result

def step(old):
    new = []
    for xs in old:
        new.append(xs.copy())
    for i in range(len(old)):
        for j in range(len(old[0])):
            if old[i][j] == '.': continue
            count = occupied_near(old, i, j)
            if old[i][j] == 'L' and count == 0:
                new[i][j] = '#'
                continue
            if old[i][j] == '#' and count >= 4:
                new[i][j] = 'L'
    return new

for xs in step(step(step(matrix))):
    print(*xs)

def equal_matrix(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                print("differs at", i, j, a[i][j], b[i][j])
                return False 
    return True

def count_seats(m):
    count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == '#':
                count += 1
    return count 

steps = 0
curr = matrix
while True:
    curr = matrix
    next = step(matrix)
    if equal_matrix(curr, next):
        break
    matrix = next
    steps += 1
print(count_seats(curr))

