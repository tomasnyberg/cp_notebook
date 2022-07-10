import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def print_board(board):
    for xs in board:
        print(xs)

def calc_score(board, i, j):
    result = board[i][j]
    for expand in range(1, len(board)):
        if i - expand >= 0 and j - expand >= 0: # top-left
            result += board[i-expand][j-expand] 
        if i - expand >= 0 and j + expand < len(board[0]): # top right
            result += board[i-expand][j+expand] 
        if i+expand < len(board) and j -expand >= 0: # bottom left
            result += board[i+expand][j-expand]
        if i+expand < len(board) and j+expand < len(board[0]): # bottom right
            result += board[i+expand][j+expand]
    return result


i = 1   
while i < len(lines):
    rows, cols = map(int, lines[i].split(" "))
    board = []
    i+=1
    while rows > 0:
        board.append(list(map(int, lines[i].split(" "))))
        rows -=1
        i+=1
    best = 0
    for c in range(len(board)):
        for d in range(len(board[0])):
            best = max(best, calc_score(board, c, d))
    print(best)
    