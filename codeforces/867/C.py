import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    x = int(line)
    print(x**2 + 10 + (x - 4) * 2)