import sys
from heapq import heappush, heappop
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict
from functools import lru_cache
ii = 1
while ii < len(lines):
    n, m = map(int, lines[ii].split())
    ii += 1
    adj_lists = {}
    for _ in range(m):
        fr, to, w = map(int, lines[ii].split())
        if fr not in adj_lists: adj_lists[fr] = {}
        if to not in adj_lists: adj_lists[to] = {}
        adj_lists[fr][to] = min(w, adj_lists[fr].get(to, 10**18))
        adj_lists[to][fr] = min(w, adj_lists[to].get(fr, 10**18))
        ii+=1
    bikespeeds = list(map(int, lines[ii].split()))
    ii+=1
    visited = {} # (node, speed) -> cost
    hq = [(0, 1, bikespeeds[0])]
    while len(hq) > 0:
        cost, node, speed = heappop(hq)
        if (node, speed) in visited: continue
        visited[(node, speed)] = cost
        for neighbor, weight in adj_lists[node].items():
            heappush(hq, (cost + weight * speed, neighbor, min(speed, bikespeeds[neighbor-1])))
    result = 10**18
    for k, v in visited.items():
        if k[0] == n:
            result = min(result, v)
    print(result)
