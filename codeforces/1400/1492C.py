import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import bisect

for i in range(0, len(lines), 3):
    n, m = map(int, lines[i].split(" "))
    a, b = lines[i+1], lines[i+2]
    n, m = len(a), len(b)
    alist, blist = list(a), list(b)
    furthest = [0] * (n + 1)
    bpointer = len(b) - 1
    for j in range(n-1, -1, -1):
        if bpointer < 0: break
        if alist[j] == b[bpointer]:
            furthest[j] = bpointer
            bpointer -= 1
        else:
            furthest[j] = furthest[j+1]
    furthest.pop()
    lastseen = {}
    for j in range(len(furthest)):
        lastseen[furthest[j]] = j
    bpointer = 0
    result = 0
    for j in range(len(a)):
        if bpointer >= len(b): break
        result = max(result, lastseen[bpointer] - j + 1 if bpointer != m-1 else lastseen[bpointer] - j)
        if alist[j] == b[bpointer]:
            bpointer += 1
    print(result)