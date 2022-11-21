import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n, a, b = map(int, lines[i].split(" "))
    print(n, a, b)
    adj_lists = {j: set() for j in range(1, n+1)}
    i+=1
    for _ in range(n-1):
        u, v, w = map(int, lines[i].split(" "))
        adj_lists[u].add((v, w))
        adj_lists[v].add((u, w))
        i+=1
    
    print(adj_lists)