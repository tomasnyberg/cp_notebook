import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split(" "))
    s = list(lines[ii+1])
    result = 0
    for start in range(k):
        seen = {}
        opposites = {}
        best = (0, 'a')
        for i in range(start, n, k):
            opposites[s[n- i - 1]] = opposites.get(s[n- i - 1], 0) + 1
            seen[s[i]] = seen.get(s[i], 0) + 1
            best = max(best, (seen[s[i]], s[i]), (opposites[s[n-i-1]], s[n-i-1]))
        for i in range(start, n, k):
            if s[i] != best[1]:
                result += 1
            s[i] = best[1]
    print(result)
