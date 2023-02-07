import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# dirs 4 directions
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(1, len(lines), 3):
    matrix = []
    matrix.append(list(map(int, lines[i+1].split(" "))))
    matrix.append(list(map(int, lines[i+2].split(" "))))
    time_til_end_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for row in range(len(matrix)):
        biggest = matrix[row][0]
        for col in range(1, len(matrix[row])):
            biggest = max(biggest+ 1, matrix[row][col] + 1)
            time_til_end_matrix[row][col] = biggest
    time_til_start_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for row in range(len(matrix)):
        biggest = matrix[row][-1]
        for col in range(len(matrix[row])-2, -1, -1):
            biggest = max(biggest + 1, matrix[row][col] + 1)
            time_til_start_matrix[row][col] = biggest
    # for xs in matrix:
    #     print(" ".join(map(str, xs)))
    # print("----")
    # for xs in time_til_end_matrix:
    #     print(" ".join(map(str, xs)))
    # print("----")
    # for xs in time_til_start_matrix:
    #     print(" ".join(map(str, xs)))
    # print()
    def score_check(i, j, time, ending_col):
        other_row = 1 - i
        # This could be a one off on the left side of the max, i think it's right though
        to_end = max(time + (len(matrix[0]) - j - 1), time_til_end_matrix[i][-1])
        to_end = max(to_end + 1, matrix[other_row][-1] + 1)
        back = max(to_end + (len(matrix[0]) - ending_col - 1), time_til_start_matrix[other_row][ending_col])
        return back
    result = 10**9
    pos = [0, 0]
    time = 0
    while pos != [1, len(matrix[0])-1 ]:
        i, j = pos
        ending_col = j
        if (j % 2 == 0 and i == 1) or (j % 2 == 1 and i == 0):
            ending_col = j + 1
        check = score_check(i, j, time, ending_col)
        # print("check", check, "pos", pos, "time", time, "ending_col", ending_col)
        result = min(check, result)
        if j % 2 == 0:
            if i == 0:
                pos[0] += 1
            else:
                pos[1] += 1
        else:
            if i == 0:
                pos[1] += 1
            else:
                pos[0] -= 1
        i, j = pos
        time = max(time + 1, matrix[i][j] + 1)
    print(result)



