import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import heapq
from collections import defaultdict
from collections import deque
# TODO Remember to add int wrapping if using dict
# lines = """3
# 6 3
# 5 5 4 5 2 2
# 3 4 5
# 2 2 5
# 1 5
# 3 4 1 6
# 4 2 6 1 5
# 0 
# 0 
# 6 2
# 1 4 4 1 5 2
# 3 6
# 4 6 3 4 5
# 4 6 5 3 4
# 0 
# 1 5
# 1 6
# 0 
# 2 1
# 4 3
# 1
# 0 
# 1 1
# """.splitlines()


results = []
idx = 0
t = int(lines[idx])
idx += 1
for _ in range(t):
    n, k = map(int, lines[idx].split())
    idx += 1
    costs = list(map(int, lines[idx].split()))
    idx += 1
    supplies = list(map(int, lines[idx].split()))
    idx += 1
    mix_recipes = []
    for _ in range(n):
        mix_recipes.append(list(map(int, lines[idx].split())))
        idx += 1
    mixings = {i: mix_recipes[i][1:] for i in range(n) if mix_recipes[i][0] > 0}
    for k, v in mixings.items():
        for i in range(len(v)):
            v[i] -=1
    graph = defaultdict(list)
    rev_graph = defaultdict(list)
    for key, values in mixings.items():
        for v in values:
            graph[v].append(key)
            rev_graph[key].append(v)
    indeg = [0] * n
    for i in range(n):
        for neighbor in graph[i]:
            indeg[neighbor] += 1
    queue = deque()
    for i in range(n):
        if indeg[i] == 0:
            queue.append(i)
    top_order = []
    while queue:
        node = queue.popleft()
        top_order.append(node)
        for neighbor in graph[node]:
            indeg[neighbor] -= 1
            if indeg[neighbor] == 0:
                queue.append(neighbor)
    min_costs = costs[:]
    for potion in supplies:
        min_costs[potion-1] = 0
    for potion in top_order:
        mix = mixings.get(potion, [])
        if mix:
            mix_cost = sum(min_costs[m] for m in mix)
            min_costs[potion] = min(min_costs[potion], mix_cost)
    print(*min_costs)