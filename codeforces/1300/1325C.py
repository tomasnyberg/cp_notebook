import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

ii = 0
while ii < len(lines):
    n = int(lines[ii])
    ii += 1
    adj_lists = {i: set() for i in range(n)}
    edges = {}
    for i in range(n - 1):
        fr, to = map(int, lines[ii].split())
        edges[(fr - 1, to - 1)] = i
        edges[(to - 1, fr - 1)] = i
        adj_lists[fr - 1].add(to - 1)
        adj_lists[to - 1].add(fr - 1)
        ii += 1
    dq = deque()
    for i in range(n):
        if len(adj_lists[i]) == 1:
            dq.append(i)
    count = 0
    result = [0] * (n - 1)
    # print(adj_lists, dq)
    while dq:
        fr = dq.popleft()
        if not adj_lists[fr]:
            continue
        # print(fr, adj_lists[fr])
        to = adj_lists[fr].pop()
        adj_lists[to].remove(fr)
        result[edges[(fr, to)]] = count
        count += 1
        if len(adj_lists[to]) == 1:
            dq.append(to)
    for i in range(n - 1):
        print(result[i])

    
    
    