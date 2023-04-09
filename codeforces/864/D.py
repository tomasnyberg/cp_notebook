import sys
lines = list(map(str.strip, sys.stdin.readlines()))

    

n, m = map(int, lines[0].split())
importances = list(map(int, lines[1].split()))
adj_lists = {i: {} for i in range(1, n+1)}
for i in range(2, n+1):
    fr, to = map(int, lines[i].split())
    adj_lists[fr][to] = 1
    adj_lists[to][fr] = 1
queries = []
for i in range(n+1, len(lines)):
    queries.append(list(map(int, lines[i].split())))

visited = set()
node_importance = {}
child_counts = {}
parents = [-1] * (n+1)
def importance_dfs(node):
    if node in visited:
        return 0
    visited.add(node)
    importance = importances[node-1]
    node_count = 1 # Keep track of the total amount of nodes in this subtree
    for adj in adj_lists[node]:
        if adj in visited: continue
        parents[adj] = node
        childimportance, childcount = importance_dfs(adj)
        adj_lists[node][adj] = childcount
        importance += childimportance
        node_count += childcount
    child_counts[node] = node_count
    node_importance[node] = importance
    return (importance, node_count)
importance_dfs(1)

# print(parents)
# The parent should not be considered a child of the node
for node in range(2, n+1):
    del adj_lists[node][parents[node]]

# for i in range(1, n+1):
#     print("node", i, "importance", node_importance[i], "parent", parents[i])
#     print("Adj lists of node", i, adj_lists[i])
#     print("Node count of node", i, child_counts[i])
#     print()

def rotate(x):
    if not adj_lists[x]: return
    max_child = max(adj_lists[x], key=lambda y: adj_lists[x][y])
    max_child_importance = node_importance[max_child]
    # Child gets all our importance - the importance of itself
    node_importance[max_child] += node_importance[x] - max_child_importance
    # We remove the importance of the child
    node_importance[x] -= max_child_importance

    max_child_nodes = child_counts[max_child]
    # Child gets all our nodes - the nodes of itself
    child_counts[max_child] += child_counts[x] - max_child_nodes
    # We remove the nodes of the child
    child_counts[x] -= max_child_nodes

    parents[max_child], parents[x] = parents[x], max_child
    adj_lists[max_child][x] = child_counts[x]
    del adj_lists[x][max_child]
    # print("max child of", x, "is", max_child)

for a, b in queries:
    if a == 2:
        rotate(b)
    else:
        print(node_importance[b])

# def rotate(x)