import sys
from collections import deque
lines = list(map(str.strip, sys.stdin.readlines()))
n = int(lines[0])

adj_lists = {i:[] for i in range(1, n+1)}
def bfs(adj_lists, start):
    visited = [False] * (len(adj_lists) + 1)
    distances = [0] * (len(adj_lists) + 1)
    visited[start] = True
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in adj_lists[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances

def max_distances(adj_lists, n):
    result = []
    for node in range(1, n + 1):
        distances = bfs(adj_lists, node)
        max_distance = max(distances[1:])
        result.append(max_distance)

    return result

height = [0 for _ in range(1, n+2)]
dist = [0 for _ in range(1, n+1)]
for i in range(1, n):
    fr, to = map(int, lines[i].split())
    adj_lists[fr].append(to)
    adj_lists[to].append(fr)

mds = max_distances(adj_lists, n)
mds.sort()
mds = deque(mds)
comps = 1
for i in range(1, n+1):
    while mds and mds[0] < i:
        mds.popleft()
        comps += 1
    if comps > n:
        comps -= 1
    print(comps, end=" ")
print()
