import sys
lines = list(map(str.strip, sys.stdin.readlines()))
test = 1
i = 1
while i < len(lines):
    N = int(lines[i])
    i+=1
    capacities = list(map(int, lines[i].split(" ")))
    capacities = [0] + capacities
    i+=1
    adj_lists = {i:set() for i in range(1,N+1)}
    for _ in range(N-1):
        fr, to = map(int, lines[i].split(" "))
        i+=1
        if capacities[fr] == capacities[to]:
            continue
        else:
            if capacities[fr] > capacities[to]:
                adj_lists[fr].add(to)
            else:
                adj_lists[to].add(fr)
    powerable = [1] * (N+1)
    visited = [False]*(N+1)
    def dfs(curr):
        visited[curr] = True
        for nbr in adj_lists[curr]:
            if visited[nbr]:
                powerable[curr] += powerable[nbr]
            else:
                powerable[curr] += dfs(nbr)
        return powerable[curr]
    for j in range(1,N+1):
        dfs(j)
    result = [-1, -1]
    for idx, x in enumerate(powerable):
        if x >= result[0]:
            result = [x, idx]
    print(f"Case #{test}: {result[0]}")
    test += 1
        
