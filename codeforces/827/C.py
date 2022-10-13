import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(2, len(lines), 9):
    matrix = []
    for j in range(i, i+8):
        matrix.append(lines[j])
    result = -1
    # for xs in matrix:
    #     print(xs)
    for xs in matrix:
        if xs == 'R'*8:
            result = 'R'
            break
    for col in range(8):
        if all([matrix[k][col] == 'B' for k in range(8)]):
            result = 'B'
            break
    print(result)
