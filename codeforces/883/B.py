import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check_win(board, symbol):
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False

for ii in range(1, len(lines), 3):
    board = []
    for i in range(3):
        board.append(list(lines[ii+i]))
    for symbol in ['X', 'O', '+']:
        if check_win(board, symbol):
            print(symbol)
            break
    else:
        print('DRAW')