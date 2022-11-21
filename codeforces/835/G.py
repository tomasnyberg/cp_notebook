import sys
lines = list(map(str.strip, sys.stdin.readlines()))
sys.setrecursionlimit(10**6)

i = 1
while i < len(lines):
    n, a, b = map(int, lines[i].split(" "))
    adj_lists = {j: set() for j in range(1, n+1)}
    i+=1
    for _ in range(n-1):
        u, v, w = map(int, lines[i].split(" "))
        adj_lists[u].add((v, w))
        adj_lists[v].add((u, w))
        i+=1
    bsums = {}
    bseen = set()
    def dfs_b(curr, score):
        bseen.add(curr)
        for nbr, wi in adj_lists[curr]:
            if nbr in bseen: continue
            if wi^score not in bsums:
                bsums[wi^score] = [nbr]
            else:
                bsums[wi^score].append(nbr)
            dfs_b(nbr, score^wi)
    dfs_b(b, 0)
    # print(bsums)
    aseen = set()
    def dfs_a(curr, score):
        aseen.add(curr)
        if score in bsums:
            return True
        for nbr, wi in adj_lists[curr]:
            if nbr == b:
                if score^wi == 0:
                    # print("We found true when we went from", curr, "to", nbr)
                    return True
            else:
                if nbr in aseen: continue
                if score ^ wi in bsums:
                    # print("We found true when we went from", curr, "to", nbr)
                    return True
                if dfs_a(nbr, score^wi):
                    return True
        return False
    print("YES" if dfs_a(a, 0) else "NO")