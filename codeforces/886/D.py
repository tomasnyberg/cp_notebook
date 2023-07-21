import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split())
    a = list(map(int, lines[ii+1].split()))
    a.sort()
    prev = a[0]
    streak = 0
    result = 0
    for x in a:
        if abs(x-prev) <= k:
            streak += 1
            result = max(result, streak)
        else:
            streak = 1
        prev = x
    print(n - result)
