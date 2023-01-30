import sys
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque
sys.setrecursionlimit(10**6)

@lru_cache(None)
def dfs(s):
    if len(s) == 0:
        return 0
    results = []
    for alice, remaining in [[s[0], s[1:]], [s[-1], s[:-1]]]:
        a = dfs(remaining[1:])
        b = dfs(remaining[:-1])
        res = max(a, b)
        if res != 0:
            results.append(res)
        else:
            if a >= 0:
                if alice > remaining[0]:
                    results.append(-1)
                elif alice < remaining[0]:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if alice > remaining[-1]:
                    results.append(-1)
                elif alice < remaining[-1]:
                    results.append(1)
                else:
                    results.append(0)
    return min(results)

for line in lines[1:]:
    # count freq of each char
    if len(line) == 2:
        print("Draw" if line[0] == line[1] else "Alice")
        continue
    freq = {}
    for c in line:
        freq[c] = freq.get(c, 0) + 1
    print("Alice" if dfs(line) == -1 else "Draw" if dfs(line) == 0 else "Bob")