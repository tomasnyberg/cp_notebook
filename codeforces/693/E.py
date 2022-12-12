import sys, bisect
lines = list(map(str.strip, sys.stdin.readlines()))

from math import ceil, log2

class segment_tree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x,y:x+y, basef=lambda x:x, basev = 0):
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.n = len(array)
        self.array = array
        self.tree = [0] * ( 2**ceil(log2(len(array))+1) - 1 )
        self.build(array)
    
    def __str__(self):
        return ' '.join([str(x) for x in self.tree])

    def _build_util(self, l, r, i, a):
        if(l==r):
            self.tree[i] = self.basef(a[l])
            return self.tree[i]
        mid = (l+r)//2
        self.tree[i] = self.merge(self._build_util(l,mid, 2*i+1, a), self._build_util(mid+1, r, 2*i+2, a))
        return self.tree[i]

    def build(self, a):
        self._build_util(0, len(a)-1, 0, a)

    def _query_util(self, i, ln, rn, l, r):
        if ln>=l and rn<=r:
            return self.tree[i]
        if ln>r or rn<l:
            return self.basev
        return self.merge( self._query_util( 2*i+1, ln, (ln+rn)//2, l, r ), self._query_util( 2*i+2, (ln+rn)//2+1, rn, l, r ) )

    def query(self, l, r):
        return self._query_util( 0, 0, self.n-1, l, r )

    def _update_util(self, i, ln, rn, x, v):
        if x>=ln and x<=rn:
            if ln != rn:
                self._update_util( 2*i+1, ln, (ln+rn)//2, x, v )
                self._update_util( 2*i+2, (ln+rn)//2 + 1, rn, x, v )
                self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
            else:
                self.tree[i] = self.basef(v)

    def update(self, x, v):
        self._update_util( 0, 0, self.n-1, x, v )   
        self.array[x] =v

def bs(xs, x, idx):
    low = 0
    high = len(xs)
    while low < high:
        mid = (low + high) >> 1
        if xs[mid][idx] <= x:
            low = mid + 1
        else:
            high = mid
    return low

i = 1
while i < len(lines):
    n = int(lines[i])
    people = []
    i+=1
    for _ in range(n):
        people.append(list(map(int, lines[i].split(" "))))
        i+=1
    by_h = [[people[j][1], people[j][0], j] for j in range(len(people))]
    by_h.sort(key=lambda x: (x[1], x[0]))
    sth = segment_tree(by_h, merge=lambda x, y: max(x,y), basef=lambda x: x, basev=[0,0,0])
    # print("By height:", by_h)
    result = [-1] * len(people)
    def try_find(h, w):
        idx = (bs(by_h, h-1, 1)) - 1
        if idx == -1: return -1
        biggest = sth.query(0, idx)
        # print("Current height, weight", h, w)
        # print("Binary search result", idx)
        # print("Query result:", sth.query(0, idx))
        if biggest[0] < w:
            return biggest[2] + 1
        else:
            return -1
    for j in range(len(people)):
        h, w = people[j]
        a = try_find(h, w)
        b = try_find(w, h)
        if a != -1:
            result[j] = a
        if b != -1:
            result[j] = b
    print(*result)