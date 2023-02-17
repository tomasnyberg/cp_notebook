import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def fill_in_min(extremes, matrix, d):
    results = [[[10**9 for _ in range(len(matrix[0]))] for _ in range(2)] for _ in range(len(extremes))]
    for idx, (row, col) in enumerate(extremes):
        steps_taken = 0
        end = len(matrix[0]) if d == 1 else -1
        for c in range(col, end, d):
            results[idx][row][c] = steps_taken
            if matrix[1-row][c] == '*':
                row = 1-row
                steps_taken += 1
            results[idx][row][c] = steps_taken
            steps_taken += 1
    return results

for i in range(1, len(lines), 3):
    matrix = [lines[i+1], lines[i+2]]
    left_mosts = []
    for c in range(len(matrix[0])):
        if matrix[0][c] == '*' or matrix[1][c] == '*':
            if matrix[0][c] == '*':
                left_mosts.append((0,c))
            if matrix[1][c] == '*':
                left_mosts.append((1,c))
            break
    right_mosts = []
    for c in range(len(matrix[0])-1, -1, -1):
        if matrix[0][c] == '*' or matrix[1][c] == '*':
            if matrix[0][c] == '*':
                right_mosts.append((0,c))
            if matrix[1][c] == '*':
                right_mosts.append((1,c))
            break
    left_mins = fill_in_min(left_mosts, matrix, 1)
    right_mins = fill_in_min(right_mosts, matrix, -1)
    # for xss in left_mins:
    #     for xs in xss:
    #         print(xs)
    #     print()
    # for xss in right_mins:
    #     for xs in xss:
    #         print(xs)
    #     print()
    result = 10**9
    results = {}
    for c in range(len(matrix[0])):
        for xss in left_mins:
            for yss in right_mins:
                for r in range(2):
                    results[(r,c)] = xss[r][c] + yss[r][c] + (1 if matrix[1-r][c] == '*' else 0)
                    result = min(result, xss[r][c] + yss[r][c] + (1 if matrix[1-r][c] == '*' else 0))
    # print(results)
    print(result)




