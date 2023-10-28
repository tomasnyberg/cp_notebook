import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque
sys.setrecursionlimit(300000)
# TODO Remember to add int wrapping if using dict

ii = 1
while ii < len(lines):
    n, marcel, valeriu = map(int, lines[ii].split())
    marcel -= 1
    valeriu -= 1
    ii += 1
    adj_lists = {i: [] for i in range(n)}
    for _ in range(n):
        fr, to = map(int, lines[ii].split())
        adj_lists[fr-1].append(to-1)
        adj_lists[to-1].append(fr-1)
        ii+=1
    visited = set()
    loop_starts = set()
    def dfs(prev, i):
        in_loop = False
        visited.add(i)
        for nbr in adj_lists[i]:
            if nbr == prev:
                continue
            if nbr in visited:
                in_loop = True
            else:
                in_loop |= dfs(i, nbr)
        if in_loop:
            loop_starts.add(i)
        return in_loop
    dfs(-1, marcel)
    def dist_to_loops(start):
        result = {}
        q = deque([start])
        visited = set()
        d = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if node in loop_starts:
                    result[node] = d
                for nbr in adj_lists[node]:
                    if nbr not in visited:
                        q.append(nbr)
            d += 1
        return result
    marcel_dist = dist_to_loops(marcel)
    valeriu_dist = dist_to_loops(valeriu)
    # print(marcel_dist)
    # print(valeriu_dist)
    for k, v in valeriu_dist.items():
        if v < marcel_dist[k]:
            print('YES')
            break
    else:
        print('NO')
    # print()