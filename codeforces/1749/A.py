import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n, m = map(int, lines[i].split())
    i += 1
    taken = set()
    