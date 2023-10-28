import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

ii = 1
while ii < len(lines):
    matrix = []
    for j in range(ii, ii+10):
        matrix.append(lines[j])
    def score(i, j):
        to_top = i+1
        to_left = j+1
        to_right = 10-j
        to_bottom = 10-i
        return min(to_top, to_left, to_right, to_bottom)
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result += score(i, j) if matrix[i][j] == "X" else 0
    print(result)
    ii+=10