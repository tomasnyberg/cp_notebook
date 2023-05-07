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

class segment_tree2:
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


import random
# array of 100 random numbers 

def test_range_sum():
    a = [random.randint(0,10000) for i in range(100000)]
    st = segment_tree(a, func=lambda x,y: x+y, basef=lambda x:x, basev=0)
    for i in range(100):
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

def test_range_min():
    a = [random.randint(0, 10000) for i in range(100000)]
    st = segment_tree2(a, lambda x, y: min(x, y), basev=float('inf'))
    for i in range(100000):
        if random.randint(0, 1):
            new_val = random.randint(0, 100)
            idx = random.randint(0, len(a)-1)
            a[idx] = new_val
            st.update(idx, new_val)
        else:
            low = random.randint(0, len(a)-1)
            high = random.randint(low, len(a)-1)
            if st.query(low, high) != min(a[low:high+1]):
                print("Error at index", i)
                break
    else:
        print("Range minimum passed")

test_range_sum()
test_range_min()