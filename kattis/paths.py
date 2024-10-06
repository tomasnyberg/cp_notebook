import sys
from functools import lru_cache
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

n, m, k = map(int, lines[0].split())
colors = list(map(int, lines[1].split()))
colors = [c - 1 for c in colors]
adj = {i: [] for i in range(n)}
for ii in range(2, len(lines)):
    u, v = map(int, lines[ii].split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)


@lru_cache(None)
def dfs(i, colors_seen):
    res = 1 if colors_seen.bit_count() > 1 else 0
    for nbr in adj[i]:
        if not (1 << colors[nbr]) & colors_seen:
            res += dfs(nbr, colors_seen | (1 << colors[nbr]))
    return res


result = 0
for i in range(n):
    result += dfs(i, 1 << colors[i])

print(result)
