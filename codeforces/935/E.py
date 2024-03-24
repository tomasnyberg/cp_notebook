import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, x = map(int, lines[ii].split())
    a = list(map(int, lines[ii+1].split()))
    a = [10**9] + a
    idx = a.index(x)
    l = 1
    r = n+1
    moves = []
    notseen = set([i for i in range(1, n+1)])
    while True:
        if r - l == 1:
            break
        m = (l + r) // 2
        notseen.discard(m)
        if a[m] <= x:
            l = m
        else:
            r = m
    if a[l] == x:
        print(0)
    else:
        print(1)
        print(l, idx)
    

        
