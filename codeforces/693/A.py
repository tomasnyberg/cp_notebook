import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    w, h, n= map(int, line.split(" "))
    sheets = 1
    while w % 2 == 0:
        w //= 2
        sheets *= 2
    while h % 2 == 0:
        h //= 2
        sheets *=2
    print("YES" if sheets >= n else "NO")