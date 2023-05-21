import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split(" "))
    s = list(lines[ii+1])
    result = 0
    bests = {i:{} for i in range(k)}
    for start in range(k):
        seen = {}
        opposites = {}
        for i in range(start, n, k):
            opposite = n-i-1
            bests[opposite % k][s[i]] = bests[opposite % k].get(s[i], 0) + 1
            bests[start][s[i]] = bests[start].get(s[i], 0) + 1
    for start in range(k):
        best = max(bests[start].items(), key=lambda x: x[1])[0]
        for i in range(start, n, k):
            opposite = n-i-1
            s[n-i-1] = best
            s[i] = best
    for i in range(n):
        if s[i] != lines[ii+1][i]:
            result += 1
    print(result)
