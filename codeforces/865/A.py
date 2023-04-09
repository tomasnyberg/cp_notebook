import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    a, b = map(int, line.split())
    print(2)
    print(a-1, 1)
    print(a, b)