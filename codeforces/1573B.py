import sys, bisect
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(2, len(lines), 3):
    a = list(map(int, lines[i].split(" ")))
    b = list(map(int, lines[i+1].split(" ")))
    bsearcharray = []
    bsearcharryindexes = []
    indexes = {}
    for idx, x in enumerate(b):
        if not bsearcharray or x > bsearcharray[-1]:
            bsearcharray.append(x)
            bsearcharryindexes.append(idx)
    best = 10**9
    for idx, x in enumerate(a):
        bsearchidx = bisect.bisect_left(bsearcharray, x+1)
        best = min(best, idx + bsearcharryindexes[bsearchidx])
    print(best)

