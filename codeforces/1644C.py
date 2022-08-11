import sys
lines = list(map(str.strip, sys.stdin.readlines()))

INF = 10**9
for i in range(1, len(lines), 2):
    n, x = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    mx = [-INF for j in range(n+1)]
    mx[0] = 0
    for l in range(n):
        s = 0
        for r in range(l, n):
            s += nums[r]
            mx[r-l+1] = max(mx[r-l+1], s)
    for k in range(n+1):
        best = max(mx)
        for l in range(1, n+1):
            best = max(best, min(l,k)*x + mx[l])
        print(best, end= " ")
    print()
