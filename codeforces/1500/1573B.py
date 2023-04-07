import sys, bisect
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(2, len(lines), 3):
    a = list(map(int, lines[i].split(" ")))
    b = list(map(int, lines[i+1].split(" ")))
    indexes = {}
    for arr in [a, b]:
        for idx, x in enumerate(arr):
            indexes[x] = idx
    l = 10**9
    ans = 10**9
    for num in range(2*len(b), 0, -1):
        if num % 2 == 0:
            l = min(l, indexes[num])
        else:
            ans = min(ans, indexes[num] + l)
    print(ans)

