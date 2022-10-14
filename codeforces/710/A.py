import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, m, x = map(int, line.split(" "))
    row = x % (n+1)
    col = x // (n+1)
    print(row, col)
    # print(row*m+col)
