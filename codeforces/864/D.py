import sys
lines = list(map(str.strip, sys.stdin.readlines()))

    

n, m = map(int, lines[0].split())
importances = list(map(int, lines[1].split()))
adj_lists = {i: set() for i in range(1, n+1)}
for i in range(2, n+2):
    fr, to = map(int, lines[i].split())
    adj_lists[fr].add(to)
    adj_lists[to].add(fr)
queries = []
for i in range(n+2, len(lines)):
    queries.append(list(map(int, lines[i].split())))

visited = set()
node_importance = {}
parents = [-1] * (n+1)
def importance_dfs(node):
    if node in visited:
        return 0
    visited.add(node)
    result = importances[node-1]
    for adj in adj_lists[node]:
        if adj in visited: continue
        parents[adj] = node
        result += importance_dfs(adj)
    node_importance[node] = result
    return result


importance_dfs(1)
for i in range(1, n+1):
    print("node", i, "importance", node_importance[i], "parent", parents[i])