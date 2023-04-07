import sys
lines = list(map(str.strip, sys.stdin.readlines()))


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
parent_M = [i for i in range(1, n+1)]
def find_M(a):
    if parent_M[a-1] == a:
        return a
    p = find_M(parent_M[a-1])
    parent_M[a-1] = p
    return p
def union_M(a, b):
    parent_M[find_M(a)-1] = parent_M[find_M(b)-1]
for i in range(1, n+1):
    for nbr in adj_lists_M[i]:
        if find_M(i) != find_M(nbr):
            union_M(i, nbr)
parent_D = [i for i in range(1, n+1)]
def find_D(a):
    if parent_D[a-1] == a:
        return a
    p = find_D(parent_D[a-1])
    parent_D[a-1] = p
    return p
def union_D(a, b):
    parent_D[find_D(a)-1] = parent_D[find_D(b)-1]
for i in range(1, n+1):
    for nbr in adj_lists_D[i]:
        if find_D(i) != find_D(nbr):
            union_D(i, nbr)
res = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: continue
        if find_M(i) != find_M(j) and find_D(i) != find_D(j):
            union_M(i, j)
            union_D(i, j)
            res.append([i, j])
print(len(res))
for fr, to in res:
    print(fr, to)