import sys
lines = list(map(str.strip, sys.stdin.readlines()))
sys.setrecursionlimit(200000)

class lca_lift:
    def __init__(self, n):
        self.n = n
        self.logn = 24
        self.depth = [0]*n
        self.edges = [[] for _ in range(n)]
        self.lift = [[-1]*self.logn for _ in range(n)]
    
    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)
    
    def attach(self, attach, attach_to):
        a = attach
        b = attach_to
        self.lift[a][0] = b
        for i in range(1, self.logn):
            if self.lift[a][i-1] == -1:
                self.lift[a][i] = -1
            else:
                self.lift[a][i] = self.lift[self.lift[a][i-1]][i-1]
        self.depth[a] = self.depth[b] + 1

    def init_lift(self, v = 0):
        self.depth[v] = 0
        self.dfs(v, -1)

    def dfs(self, v, p):
        self.lift[v][0] = p
        for i in range(1, self.logn):
            if self.lift[v][i-1] == -1:
                self.lift[v][i] = -1
            else:
                self.lift[v][i] = self.lift[self.lift[v][i-1]][i-1]
        for u in self.edges[v]:
            if u != p:
                self.depth[u] = self.depth[v] + 1
                self.dfs(u, v)

    def get(self, v, k):
        for i in range(self.logn-1, -1,-1):
            if v == -1:
                return -1
            if (1 << i) <= k:
                v = self.lift[v][i]
                k -= (1 << i)
        return v

    def get_lca(self, a, b):
        if self.depth[a] < self.depth[b]:
            a, b = b, a
        d = self.depth[a] - self.depth[b]
        v = self.get(a, d)
        if v == b:
            return v
        else:
            for i in range(self.logn-1, -1, -1):
                if self.lift[v][i] != self.lift[b][i]:
                    v = self.lift[v][i]
                    b = self.lift[b][i]
            return self.lift[b][0]

    def get_dist(self, a, b):
        lca = self.get_lca(a, b)
        return self.depth[a] + self.depth[b] - 2 * self.depth[lca]

class centroid:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.vis = [False]*n
        self.par = [-1]*n
        self.sz = [0]*n
    
    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)
    
    def find_size(self, v, p=-1):
        if self.vis[v]:
            return 0
        self.sz[v] = 1
        for u in self.edges[v]:
            if u != p:
                self.sz[v] += self.find_size(u, v)
        return self.sz[v]
    
    def find_centroid(self, v, p, n):
        for u in self.edges[v]:
            if u != p and not self.vis[u] and self.sz[u] > n//2:
                return self.find_centroid(u, v, n)
        return v

    def init_centroid(self, v = 0, p =-1):
        self.find_size(v)
        c = self.find_centroid(v, -1, self.sz[v])
        self.vis[c] = True
        self.par[c] = p
        for u in self.edges[c]:
            if not self.vis[u]:
                self.init_centroid(u, c)

lca_tree = lca_lift(100005)
centroid_tree = centroid(100005)
best = [10**9]*100005
def update(v):
    best[v] = 0
    u = v
    while centroid_tree.par[u] != -1:
        u = centroid_tree.par[u]
        best[u] = min(best[u], lca_tree.get_dist(v, u))

def query(v):
    ans = best[v]
    u = v
    while centroid_tree.par[u] != -1:
        u = centroid_tree.par[u]
        ans = min(ans, best[u] + lca_tree.get_dist(v, u))
    return ans

n, q = map(int, lines[0].split())
for i in range(n-1):
    u, v = map(int, lines[i+1].split())
    u -= 1
    v -= 1
    lca_tree.add_edge(u, v)
    centroid_tree.add_edge(u, v)
try:

    lca_tree.init_lift()
    centroid_tree.init_centroid()
    update(0)
    for i in range(q):
        t, v = map(int, lines[n+i].split())
        v -= 1
        if t == 1:
            update(v)
        else:
            print(query(v))
# If we get an exception ,print it
except Exception as e:
    print(e)
