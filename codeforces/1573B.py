from operator import index
import sys, bisect
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(2, len(lines), 3):
    a = list(map(int, lines[i].split(" ")))
    b = list(map(int, lines[i+1].split(" ")))
    bsorted = list(sorted(b))
    indexes = {}
    for idx, x in enumerate(bsorted):
        indexes[x] = idx
    best = 10**9
    for idx, x in enumerate(a):
        if x < b[0]:
            best = min(best, idx)
            continue
        smallest_bigger_idx = bisect.bisect_left(bsorted, x+1)
        candidate = idx + indexes[bsorted[smallest_bigger_idx]]
        best = min(best, candidate)
    print(best)

