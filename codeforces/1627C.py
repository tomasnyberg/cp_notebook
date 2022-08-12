import sys, threading

sys.setrecursionlimit(10**9)
threading.stack_size(10**8)
def solve():
    lines = list(map(str.strip, sys.stdin.readlines()))
    i = 1
    while i < len(lines):
        n = int(lines[i])
        i+=1
        degree = {j: 0 for j in range(1, n+1)}
        adj_lists = {j: [] for j in range(1, n+1)}
        edges = []
        while n > 1:
            fr, to = map(int, lines[i].split(" "))
            adj_lists[fr].append(to)
            adj_lists[to].append(fr)
            degree[fr]+=1
            degree[to]+=1
            edges.append([fr, to])
            n -= 1
            i+=1
        if any([degree[key] >= 3 for key in degree]):
            print(-1)
            continue
        last_taken = {j:-1 for j in range(1, len(degree) + 1)}
        edge_weight = {}
        visited = set()
        def dfs(curr, previouslytaken):
            visited.add(curr)
            for nbr in adj_lists[curr]:
                if nbr not in visited:
                    edgestr = str(curr) + " " + str(nbr)
                    edgestr2 = str(nbr) + " " + str(curr)
                    weight = 2 if previouslytaken == -1 or previouslytaken == 5 else 5
                    edge_weight[edgestr] = weight 
                    edge_weight[edgestr2] = weight
                    previouslytaken = weight
                    dfs(nbr, weight)
        try:
            dfs(1, -1)
        except Exception as e:
            print(e)
        for fr, to in edges:
            print(edge_weight[str(fr) + " " + str(to)], end=" ")
        print()

threading.Thread(target=solve).start()