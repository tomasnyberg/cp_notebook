import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for x in lines[1:]:
    print(9 * (len(x) - 1) + int(x[0]))
