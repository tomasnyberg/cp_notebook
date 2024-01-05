import sys
from functools import lru_cache
from collections import Counter
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    counts = dict(Counter(line))
    for c in counts:
        if counts[c] > len(line) // 2:
            print(counts[c] - (len(line) - counts[c]))
            break
    else:
        print(0 if len(line) % 2 == 0 else 1)