import sys
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque 
MOD = 998244353

def sieve(num):
    prime = [True for i in range(num+1)]
    result = set()
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            result.add(p)
    return result

first_10 = sieve(20)
print(first_10)

l, r  = 1, 10**6
adj = [[] for _ in range(10**6)]
for i in range(l, r+1):
    for j in range(i*2, r+1, i):
        adj[i-l].append(j-l)

def bfs(l, r):
    dq = deque([0])
    dist = [0 for _ in range(r-l+1)]
    while dq:
        u = dq.pop(0)
        for v in adj[u]:
            if dist[v] == 0:
                dist[v] = dist[u] + 1
                dq.append(v)
    return dist


for line in lines[1:]:
    l, r = map(int, line.split())