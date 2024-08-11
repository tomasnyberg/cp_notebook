import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
sys.setrecursionlimit(10**6)
# TODO Remember to add int wrapping if using dict

ii = 1
while ii < len(lines):
    n, k = map(int, lines[ii].split())
    ii += 1
    matrix = []
    for _ in range(k):
        matrix.append(list(map(int, lines[ii].split())))
        ii += 1
    adj = {i: set() for i in range(1, n + 1)}
    bad = False
    for i in range(k):
        for j in range(1, n-1):
            adj[matrix[i][j]].add(matrix[i][j+1])
    topsort = []
    visited = set()

    def dfs(x):
        if x in visited:
            return
        visited.add(x)
        for nbr in adj[x]:
            dfs(nbr)
        topsort.append(x)
    for i in range(1, n + 1):
        dfs(i)
    topsort = topsort[::-1]
    indices = {x: i for i, x in enumerate(topsort)}
    for i in range(len(topsort)):
        for nbr in adj[topsort[i]]:
            if indices[nbr] < i:
                bad = True
                break
    print('YES' if not bad else 'NO')
