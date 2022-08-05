import sys
lines = list(map(str.strip, sys.stdin.readlines()))

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

for i in range(2, len(lines), 4):
    a = list(map(int, lines[i].split(" ")))
    b = list(map(int, lines[i+1].split(" ")))
    c = list(map(int, lines[i+2].split(" ")))
    adj_lists = {j: set() for j in range(len(a))}
    bad_nodes = set()
    for j in range(len(a)):
        adj_lists[a[j]-1].add(b[j]-1)
        adj_lists[b[j]-1].add(b[j]-1)
        if c[j] != 0 or a[j] == b[j]:
            bad_nodes.update([a[j]-1, b[j]-1, c[j]-1])
    
    sccs = union_find(adj_lists, len(a))
    result = 1
    for scc in sccs:
        if len(scc) == 1: continue
        good = True
        for x in scc:
            if x in bad_nodes:
                good = False
                break
        if good: result *=2
    # print(sccs)
    print(result%(10**9+7))
    

    # print()
        



    # print()


