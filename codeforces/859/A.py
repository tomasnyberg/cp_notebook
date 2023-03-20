import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    a, b, c = map(int, line.split())
    if a + b == c:
        print("+")
    else:
        print("-")