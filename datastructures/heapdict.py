try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping

class heapdict(MutableMapping):
    __marker = object()

    def __init__(self, *args, **kw):
        self.heap = []
        self.d = {}
        self.update(*args, **kw)

    def clear(self):
        del self.heap[:]
        self.d.clear()

    def __setitem__(self, key, value):
        if key in self.d:
            self.pop(key)
        wrapper = [value, key, len(self)]
        self.d[key] = wrapper
        self.heap.append(wrapper)
        self._decrease_key(len(self.heap)-1)

    def _min_heapify(self, i):
        n = len(self.heap)
        h = self.heap
        while True:
            # calculate the offset of the left child
            l = (i << 1) + 1
            # calculate the offset of the right child
            r = (i + 1) << 1
            if l < n and h[l][0] < h[i][0]:
                low = l
            else:
                low = i
            if r < n and h[r][0] < h[low][0]:
                low = r

            if low == i:
                break

            self._swap(i, low)
            i = low

    def _decrease_key(self, i):
        while i:
            # calculate the offset of the parent
            parent = (i - 1) >> 1
            if self.heap[parent][0] < self.heap[i][0]:
                break
            self._swap(i, parent)
            i = parent

    def _swap(self, i, j):
        h = self.heap
        h[i], h[j] = h[j], h[i]
        h[i][2] = i
        h[j][2] = j

    def __delitem__(self, key):
        wrapper = self.d[key]
        while wrapper[2]:
            # calculate the offset of the parent
            parentpos = (wrapper[2] - 1) >> 1
            parent = self.heap[parentpos]
            self._swap(wrapper[2], parent[2])
        self.popitem()

    def __getitem__(self, key):
        return self.d[key][0]

    def __iter__(self):
        return iter(self.d)

    def popitem(self):
        """D.popitem() -> (k, v), remove and return the (key, value) pair with lowest\nvalue; but raise KeyError if D is empty."""
        wrapper = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
        else:
            self.heap[0] = self.heap.pop()
            self.heap[0][2] = 0
            self._min_heapify(0)
        del self.d[wrapper[1]]
        return wrapper[1], wrapper[0]

    def __len__(self):
        return len(self.d)

    def ksmallest(self, k):
        if k > len(self.d):
            raise Exception("k is larger than the length of the heapdict")
        largest = [self.popitem() for i in range(k)]
        for i in largest:
            self[i[0]] = i[1]
        return largest

    def peekitem(self):
        """D.peekitem() -> (k, v), return the (key, value) pair with lowest value;\n but raise KeyError if D is empty."""
        return (self.heap[0][1], self.heap[0][0])
# NOTE: The heapdict works as follows: Key -> Priority.
# This means you can't do something like this
hd = heapdict()
hd[-5] = 1
hd[-2] = 1
# Where you are keeping track of how many elems of some kind you have, and also want to know the smallest one at any given time

# What you will need to do instead is something like this
hd = heapdict()
hd[-71] = [-73, 2]
hd[-31] = [-100, 2]
print(hd.peekitem())