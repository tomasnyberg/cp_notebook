from math import ceil, log2

class segment_tree:
    def __init__(self, arr, func= lambda x,y: x+y, basef=lambda x:x, basev=0):
        self.n = len(arr)
        self.func = func
        self.basef = basef
        self.basev = basev
        self.tree = [0]*(4 * self.n)
        self.lazy = [0]*(4 * self.n)
        self.build_tree(arr, 1, 0, self.n - 1)

    def build_tree(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build_tree(arr, 2 * node, start, mid)
            self.build_tree(arr, 2 * node + 1, mid + 1, end)
            self.tree[node] = self.func(self.tree[2 * node], self.tree[2 * node + 1])

    def _update_range(self, node, start, end, l, r, val):
        if self.lazy[node] != 0:
            self.tree[node]= self.func(self.tree[node], self.lazy[node]*(end - start + 1)) # this will have to change for min / max
            if start != end:
                self.lazy[2 * node] = self.func(self.lazy[2 * node], self.lazy[node])
                self.lazy[2 * node + 1] = self.func(self.lazy[2 * node + 1], self.lazy[node])
            self.lazy[node] = 0
        if start > end or start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[node] = self.func(self.tree[node], val*(end - start + 1)) # this will have to change for min / max
            if start != end:
                self.lazy[2 * node] = self.func(self.lazy[2 * node], val)
                self.lazy[2 * node + 1] = self.func(self.lazy[2 * node + 1], val)
            return
        mid = (start + end) // 2
        self._update_range(2 * node, start, mid, l, r, val)
        self._update_range(2 * node + 1, mid + 1, end, l, r, val)
        self.tree[node] = self.func(self.tree[2 * node], self.tree[2 * node + 1])

    def _query_range(self, node, start, end, l, r):
        if start > end or start > r or end < l:
            return 0
        if self.lazy[node] != 0:
            self.tree[node] = self.func(self.tree[node], self.lazy[node]*(end - start + 1)) # this will have to change for min / max
            if start != end:
                self.lazy[2 * node] = self.func(self.lazy[2 * node], self.lazy[node])
                self.lazy[2 * node + 1] = self.func(self.lazy[2 * node + 1], self.lazy[node])
            self.lazy[node] = 0
        if start >= l and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self._query_range(2 * node, start, mid, l, r)
        p2 = self._query_range(2 * node + 1, mid + 1, end, l, r)
        return self.func(p1, p2)

    def update(self, i, val):
        self._update_range(1, 0, self.n - 1, i, i, val)

    def update_range(self, l, r, val):
        self._update_range(1, 0, self.n - 1, l, r, val)

    def query(self, l, r):
        return self._query_range(1, 0, self.n - 1, l, r)

import random
# array of 100 random numbers 

def test_range_sum():
    a = [random.randint(0,10000) for i in range(100000)]
    st = segment_tree(a, func=lambda x,y: x+y, basef=lambda x:x, basev=0)
    for i in range(100000):
        if random.randint(0,1):
            new_val = random.randint(0,100)
            low = random.randint(0,len(a)-1)
            high = random.randint(low,len(a)-1)
            for idx in range(low,high+1):
                a[idx] += new_val
            st.update_range(low, high, new_val)
            # update the value at index i to a random number
        else:
            low = random.randint(0,len(a)-1)
            high = random.randint(low,len(a)-1)
            if st.query(low, high) != sum(a[low:high+1]):
                print("Error at index", i)
                break
    else:
        print("Range sum passed")

test_range_sum()