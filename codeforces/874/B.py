import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for ii in range(1, len(lines), 3):
    n, k = map(int, lines[ii].split(" "))
    a = list(map(int, lines[ii+1].split(" ")))
    b = list(map(int, lines[ii+2].split(" ")))
    a = list(enumerate(a))
    ans = [0 for _ in range(n)]
    a.sort(key=lambda x: x[1])
    b.sort()
    for i in range(n):
        ans[a[i][0]] = b[i]
    print(*ans)
