import sys
lines = list(map(str.strip, sys.stdin.readlines()))

matrix = []
for line in lines:
    matrix.append(line)

def check(down, right):
    result = 0
    row = down
    col = right
    while row < len(matrix):
        if matrix[row][col] == '#':
            result += 1
        row += down
        col += right
        col %= len(matrix[0])
    return result

print("Part one answer:", check(1, 3))
total = 1
for r, d in [[1, 1], [3,1], [5,1], [7,1], [1,2]]:
    total *= check(d, r)
print("Part two anser:", total)
