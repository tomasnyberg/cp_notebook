import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for ii in range(1, len(lines), 2):
    n, x = map(int, lines[ii].split())
    a = list(map(int, lines[ii+1].split()))
    idx = a.index(x)
    l = 0
    r = n
    while r-l != 1:
        m = (l + r) // 2
        if a[m] <= x:
            l = m
        else:
            r = m
    if a[l] == x:
        print(0)
    else:
        print(1)
        print(l + 1, idx + 1)
