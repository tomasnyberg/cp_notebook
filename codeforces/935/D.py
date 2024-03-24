import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict


for ii in range(1, len(lines), 3):
    n, m = map(int, lines[ii].split())
    a = list(map(int, lines[ii+1].split()))
    b = list(map(int, lines[ii+2].split()))
    smallest = [10**18, -1]
    taken = 0
    extra = 0
    for i in range(n-1,-1,-1):
        taken += min(a[i], b[i])
        if (i+1) <= m:
            smallest = min(smallest, [a[i] + extra, i])
            extra += b[i]
    idx = smallest[1]
    for i in range(idx):
        taken -= min(a[i], b[i])
    # print(taken, smallest)
    print(taken - min(a[idx], b[idx]) + a[idx])

