import sys
from collections import deque
lines = list(map(str.strip, sys.stdin.readlines()))
n = int(lines[0])

adj_lists = {i:[] for i in range(1, n+1)}

height = [0 for _ in range(1, n+2)]
dist = [0 for _ in range(1, n+1)]
for i in range(1, n):
    fr, to = map(int, lines[i].split())
    adj_lists[fr].append(to)
    adj_lists[to].append(fr)

def bfs(start):
    depth = 0
    q = deque([start])
    visited = {}
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node not in visited:
                visited[node] = depth
                for child in adj_lists[node]:
                    if child not in visited:
                        q.append(child)
        depth += 1
    return visited

deepest = max(bfs(1).items(), key=lambda x: x[1])[0]
deepestbfs = bfs(deepest)
other = max(deepestbfs.items(), key=lambda x: x[1])[0]
otherbfs = bfs(other)

furthest = [0]*(n+1)
for i in range(1, n+1):
    furthest[i] = max(deepestbfs[i], otherbfs[i])
furthest.sort()
furthest = deque(furthest)
furthest.popleft()
components = 1
for i in range(n):
    while furthest and i >= furthest[0]:
        components += 1
        furthest.popleft()
    if components == n+1:
        components -= 1
    print(components, end=" ")
print()    
