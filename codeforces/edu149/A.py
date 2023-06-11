import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    x, k = map(int, line.split())
    if x % k == 0:
        print(2)
        print(1, x - 1)
    else:
        print(1)
        print(x)