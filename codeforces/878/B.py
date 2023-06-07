import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, k = map(int, line.split())
    if k >= 33:
        print(n+1)
    else:
        print(min(n, (1 << k) - 1) + 1)