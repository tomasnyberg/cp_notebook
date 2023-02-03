import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for s in lines[2::2]:
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    othercounts = {}
    result = 0
    for c in s:
        othercounts[c] = othercounts.get(c, 0) + 1
        counts[c] -= 1
        if counts[c] == 0:
            del counts[c]
        result = max(result, len(counts) + len(othercounts))
    print(result)
        
