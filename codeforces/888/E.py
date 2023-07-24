import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import heapq
# TODO Remember to add int wrapping if using dict

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
    min_costs = costs[:]
    for potion in supplies:
        min_costs[potion-1] = 0
    queue = [(cost, idx) for idx, cost in enumerate(min_costs)]
    heapq.heapify(queue)
    visited = set()
    while queue:
        cost, potion = heapq.heappop(queue)
        if potion in visited:
            continue
        visited.add(potion)
        mix = mixings.get(potion, [])
        if mix:
            mix_cost = sum(min_costs[m-1] for m in mix)
            if mix_cost < min_costs[potion]:
                min_costs[potion] = mix_cost
                heapq.heappush(queue, (mix_cost, potion))
    print(*min_costs)