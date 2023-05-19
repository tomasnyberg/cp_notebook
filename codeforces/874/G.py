import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

ii = 1
while ii < len(lines):
    n = int(lines[ii])
    adj_lists = [[] for _ in range(n)]
    ii += 1
    edge_indices = {}
    idx = 1
    for _ in range(n - 1):
        u, v = map(int, lines[ii].split(" "))
        adj_lists[u-1].append(v-1)
        adj_lists[v-1].append(u-1)
        edge_indices[(u-1, v-1)] = idx
        edge_indices[(v-1, u-1)] = idx
        idx += 1
        # TODO remember which edges were cut
        ii += 1
    if n < 3:
        print(-1)
        continue
    parents = [-1 for _ in range(n)]
    parents[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        adj_lists[u] = [v for v in adj_lists[u] if parents[v] == -1]
        for v in adj_lists[u]:
            parents[v] = u
            q.append(v)
    parents_uf = [i for i in range(n)]
    sizes = [1 for _ in range(n)]
    def find(parent, i):
        if parent[i] == i:
            return i
        parent[i] = find(parent, parent[i])
        return parent[i]
    def union(parent, size, x, y):
        root_x = find(parent, x)
        root_y = find(parent, y)
        if root_x == root_y:
            return
        if size[root_x] < size[root_y]:
            parent[root_x] = root_y
            size[root_y] += size[root_x]
        else:
            parent[root_y] = root_x
            size[root_x] += size[root_y]
    q = deque()
    for i in range(len(adj_lists)):
        if len(adj_lists[i]) == 0:
            q.append(i)
    cuts = []
    visited = set()
    while q:
        u = q.popleft()
        if u == 0 or u in visited: continue
        visited.add(u)
        if sizes[find(parents_uf, u)] < 3:
            union(parents_uf, sizes, u, parents[u])
        else:
            cuts.append(edge_indices[(u, parents[u])])
        q.append(parents[u])
    if any([x > 3 for x in sizes]):
        print(-1)
    else:
        print(len(cuts))
        print(*cuts)
    # print(-1 if any([x > 3 for x in sizes]) else cuts)


        