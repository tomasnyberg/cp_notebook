import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def union_find(adj_lists, n):
    parent = [i for i in range(1, n+1)]
    def union(a, b):
        parent[find(a)-1] = parent[find(b)-1]
    def find(a):
        if parent[a-1] == a:
            return a
        p = find(parent[a-1])
        parent[a-1] = p
        return p
    for i in range(1, n+1):
        for nbr in adj_lists[i]:
            if find(i) != find(nbr):
                union(i, nbr)
    sccs = {}
    for idx, x in enumerate(parent):
        idx += 1
        p = find(x)
        if p not in sccs: sccs[p] = []
        sccs[find(x)].append(idx)
    scc_arr = []
    for key in sccs:
        scc_arr.append(sccs[key])
    return scc_arr

n, a, b = map(int, lines[0].split(" "))
adj_lists_M = {i:set() for i in range(1, n+1)}
adj_lists_D = {i:set() for i in range(1, n+1)}
i = 1
while a > 0:
    fr, to = map(int, lines[i].split(" "))
    adj_lists_M[fr].add(to)
    adj_lists_M[to].add(fr)
    a-=1
    i+=1
while b > 0:
    fr, to = map(int, lines[i].split(" "))
    adj_lists_D[fr].add(to)
    adj_lists_D[to].add(fr)
    b-=1
    i+=1
print(adj_lists_D)
print(adj_lists_M)

print(union_find(adj_lists_D, n))
print(union_find(adj_lists_M, n))