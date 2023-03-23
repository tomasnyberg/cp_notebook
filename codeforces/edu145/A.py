import sys
import itertools
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    counts = {}
    for c in line:
        counts[c] = counts.get(c, 0) + 1
    if len(counts) == 1:
        print(-1)
    elif len(counts) == 2:
        if counts[line[0]] == 2:
            print(4)
        else:
            print(6)
    else:
        print(4)

