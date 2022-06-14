import sys
lines = list(map(str.strip, sys.stdin.readlines()))


a = 2
while a < len(lines):
    board = []
    for j in range(a, a+8):
        board.append(lines[j])
    for i in range(1, 7):
        for j in range(1, 7):
            if board[i][j] == '#' and board[i-1][j-1] == '#' and board[i-1][j+1] == '#' and board[i+1][j+1] == '#' and board[i+1][j-1] == '#':
                print(i+1, j+1)
    a+=9