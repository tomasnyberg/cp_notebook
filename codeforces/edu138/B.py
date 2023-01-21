import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    n = int(lines[i])
    a = list(map(int, lines[i+1].split()))
    b = list(map(int, lines[i+2].split()))
    print(sum(a) + sum(b) - max(b))
