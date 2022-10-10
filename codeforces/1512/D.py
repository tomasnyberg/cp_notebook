import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    b = list(map(int, line.split(" ")))
    total = sum(b)
    b.sort()
    badindex = -1
    for idx1, candidate in enumerate(b[len(b)-5:]):
        for idx, num in enumerate(b[:-2]):
            if total - num - candidate == candidate:
                badindex = idx
                break
        if badindex != -1:
            break
    if sum(b[:-2]) == b[-2]:
        badindex = len(b) - 2
    if sum(b[:-2]) == b[-1]:
        badindex = len(b) - 1
    if badindex == -1:
        print(-1)
        continue
    del b[badindex]
    b.pop()
    print(*b)