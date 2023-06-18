import sys
lines = list(map(str.strip, sys.stdin.readlines()))

from functools import lru_cache

sys.setrecursionlimit(320000)

ii = 1
while ii < len(lines):
    n = int(lines[ii])
    adj_lists = {i:[] for i in range(1, n + 1)}
    ii += 1
    for i in range(n- 1):
        fr, to = map(int, lines[ii + i].split())
        adj_lists[fr].append(to)
        adj_lists[to].append(fr)
    ii += n - 1
    q = int(lines[ii])
    ii += 1
    queries = []
    for i in range(q):
        queries.append(list(map(int, lines[ii + i].split())))
    ii += q
    ways_to_leaves = [0] * (n + 1)
    visited = {}
    def dfs(curr):
        if curr in visited:
            return visited[curr]
        visited[curr] = 0
        if len(adj_lists[curr]) == 1 and curr != 1:
            visited[curr] = 1
            return 1
        else:
            visited[curr] = sum(dfs(child) for child in adj_lists[curr] if child not in visited)
            return visited[curr]
    dfs(1)
    for a, b in queries:
        print(dfs(a) * dfs(b))