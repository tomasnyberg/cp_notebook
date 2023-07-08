import sys
from collections import deque
from heapq import heappush, heappop
lines = list(map(str.strip, sys.stdin.readlines()))

ii = 1
while ii < len(lines):
    n, m = map(int, lines[ii].split())
    ii += 1
    symptoms = int(lines[ii], 2)
    ii += 1
    medicines = []
    for _ in range(m):
        days = int(lines[ii])
        removes = int(lines[ii+1],2)
        adds = int(lines[ii+2], 2)
        medicines.append((days, removes, adds))
        ii += 3
    adj_lists = {i:{} for i in range(1 << n)}
    for state in range(1 << n):
        for d, remove, add in medicines:
            target = (state & ~remove) | add
            adj_lists[state][target] = min(adj_lists[state].get(target, float('inf')), d)
    hq = [(0, symptoms)]
    found = False
    visited = set()
    while hq:
        d, state = heappop(hq)
        if state == 0:
            found = True
            print(d)
            break
        if state in visited:
            continue
        visited.add(state)
        for nbr in adj_lists[state]:
            heappush(hq, (d + adj_lists[state][nbr], nbr))
    if not found:
        print(-1)

