import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split(" "))
    s = list(lines[ii+1])
    result = 0
    for start in range(k):
        best = {}
        for i in range(start, n, k):
            opposite = n-1-i
            if opposite != i:
                best[s[opposite]] = best.get(s[opposite], 0) + 1
            best[s[i]] = best.get(s[i], 0) + 1
        to_put = max(best.items(), key=lambda x: x[1])[0]
        for i in range(start, n, k):
            opposite = n-1-i
            if s[i] != to_put:
                result += 1
                s[i] = to_put
            if s[opposite] != to_put:
                result += 1
                s[opposite] = to_put
    print(result)
