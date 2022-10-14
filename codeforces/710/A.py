import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, m, x = map(int, line.split(" "))
    row = x % n if x % n != 0 else n
    col = math.ceil(x / (n))
    # print(x, "is at row", row, "col", col)
    print((row-1)*m+col)
