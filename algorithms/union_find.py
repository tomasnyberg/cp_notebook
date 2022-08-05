# Finds all the strongly connected components in an undirected graph given the adjacency lists
# Note: expects the nodes to be 0 based, a lot of problems go from 1

def union_find(adj_lists, n):
    parent = [i for i in range(n)]
    def union(a, b):
        parent[find(a)] = parent[find(b)]
    def find(a):
        if parent[a] == a:
            return a
        p = find(parent[a])
        parent[a] = p
        return p
    for i in range(n):
        for nbr in adj_lists[i]:
            if find(i) != find(nbr):
                union(i, nbr)
    sccs = {}
    for idx, x in enumerate(parent):
        p = find(x)
        if p not in sccs: sccs[p] = []
        sccs[find(x)].append(idx)
    scc_arr = []
    for key in sccs:
        scc_arr.append(sccs[key])
    return scc_arr