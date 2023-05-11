import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import bisect

for i in range(0, len(lines), 3):
    n, m = map(int, lines[i].split(" "))
    s, p = lines[i+1], lines[i+2]
    pos = 0
    a, b = [], []
    for i in range(m):
        while s[pos] != p[i]:
            pos += 1
        a.append(pos)
        pos += 1
    pos = n-1
    for i in range(m-1, -1, -1):
        while s[pos] != p[i]:
            pos -= 1
        b.append(pos)
        pos -= 1
    b.reverse()
    best = 0
    for i in range(m-1):
        best = max(best, b[i+1]-a[i])
    print(best)
        