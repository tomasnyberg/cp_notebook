import sys
from bisect import bisect_left
lines = list(map(str.strip, sys.stdin.readlines()))
# lines = open('./codeforces/933/in').read().strip().split('\n')
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 4):
    n, m, k = map(int, lines[ii].split())
    a = list(map(int, lines[ii + 1].split()))
    b = list(map(int, lines[ii + 2].split()))
    c = list(map(int, lines[ii + 3].split()))
    maxd = [0,-1]
    for i in range(1, len(a)):
        if a[i] - a[i-1] > maxd[0]:
            maxd = [a[i] - a[i-1], i]
    b = sorted(set(b))
    c = list(sorted(set(c)))
    low = 0
    high = maxd[0]
    lb = a[maxd[1] - 1]
    rb = a[maxd[1]]
    in_c = set(c)
    def check(mid):
        for x in b:
            lt = lb + mid
            gt = rb - mid
            target = gt - x
            idx = bisect_left(c, target)
            for d in range(-5, 5):
                if 0 <= idx + d < len(c) and x + c[idx+d] <= lt and x + c[idx+d] >= gt:
                    return True
        return False
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            high = mid
        else:
            low = mid + 1
    a.append(a[maxd[1]-1] + low)
    a.sort()
    maxd = 0
    for i in range(1, len(a)):
        maxd = max(maxd, a[i] - a[i-1])
    print(maxd)