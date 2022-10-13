import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(2, len(lines), 10):
    matrix = []
    for j in range(i+1, i+9):
        matrix.append(lines[j])
    result = -1
    for xs in matrix:
        if xs == 'R'*8:
            result = 'R'
            break
        if xs == 'B'*8:
            result = 'B'
            break
    for col in range(8):
        if all([matrix[i][col] == 'R' for i in range(8)]):
            result = 'R'
            break
        if all([matrix[i][col] == 'B' for i in range(8)]):
            result = 'B'
            break
    print(result)
