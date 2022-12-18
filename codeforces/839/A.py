import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    print(eval(line))