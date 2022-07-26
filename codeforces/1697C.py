import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(2, len(lines), 3):
    s = lines[i]
    t = lines[i+1]
    print(s)
    print(t)
    print()