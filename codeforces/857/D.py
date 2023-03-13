import sys
lines = list(map(str.strip, sys.stdin.readlines()))

import math

class Container(object):
	"""Base class of SortedList"""
	def __init__(self, data=None):
		super(Container, self).__init__()
		self.data = data[:] if data else []

	def __repr__(self):
		return '%s(%s)' % (self.__class__.__name__, repr(self.data))
	def __str__(self):
		return str(self.data)
	def __unicode__(self):
		return unicode(self.data)

	def __cast(self, other):
		if isinstance(other, Container): return other.data
		else: return other
	def __lt__(self, other):
		return self.data < self.__cast(other)
	def __le__(self, other):
		return self.data <= self.__cast(other)
	def __eq__(self, other):
		return self.data == self.__cast(other)
	def __ne__(self, other):
		return self.data != self.__cast(other)
	def __gt__(self, other):
		return self.data > self.__cast(other)
	def __ge__(self, other):
		return self.data >= self.__cast(other)
	def __cmp__(self, other):
		return cmp(self.data, self.__cast(other))
	def __hash__(self):
		return hash(self.data)

	def __len__(self):
		return len(self.data)

	def __getitem__(self, key):
		return self.data[key]
	def __setitem__(self, key, value):
		self.data[key] = value
	def __delitem__(self, key):
		del self.data[key]

	def __iter__(self):
		return self.data.__iter__()
	def __reversed__(self):
		return reversed(self.data)

	def __contains__(self, item):
		return item in self.data

from bisect import bisect_left, bisect_right
import bisect

class SortedList(Container):
	def __init__(self, data=None):
		self.data = sorted(data) if data else []

	def __setitem__(self, key, value):
		raise NotImplementedError

	def __contains__(self, value):
		return bisect_right(self.data, value) > 0

	def add(self, value):
		"""Add an item to this list."""
		index = bisect_right(self.data, value)
		self.data.insert(index, value)

	def pop(self, index=None):
		"""Remove and return item at index (default last).
		Raise IndexError if this list is empty."""
		if index is None:
			index = len(self.data) - 1
		return self.data.pop(index)

	def remove(self, value):
		"""Remove first occurrence of value.
		Raise ValueError if not found."""
		index = self.index(value)
		del self[index]

	def clear(self):
		"""Remove all items from this list."""
		self.data = []

	def copy(self):
		"""Return a shallow copy of this list."""
		return self.__class__(self.data[:])

	def count(self, value):
		"""Return number of occurrences of value."""
		i = bisect_left(self.data, value)
		j = bisect_right(self.data, value)
		return j - i

	def index(self, value, start=0, stop=None):
		"""Return first index of value.
		Raise ValueError if not found."""
		if stop is None:
			stop = len(self.data)
		index = bisect_left(self.data, value, start, stop)
		if index != len(self.data) and self.data[index] == value:
			return index
		raise ValueError

from math import log2

def build_sparse_table(arr):
    n = len(arr)
    logn = int(log2(n)) + 3
    st = [[0 for j in range(logn)] for i in range(n)]
    for i in range(n):
        st[i][0] = arr[i]
    for j in range(1, logn):
        for i in range(n - (1 << j) + 1):
            st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
    return st

def query_sparse_table(st, l, r):
    j = int(log2(r - l + 1))
    return max(st[l][j], st[r - (1 << j) + 1][j])

i = 1
while i < len(lines):
    n = int(lines[i])
    a = []
    b = []
    i+=1
    for _ in range(n):
        x, y = map(int, lines[i].split())
        a.append(x)
        b.append(y)
        i+=1
    low = 0
    high = len(a) - 1
    ab = [(x,y) for x, y in zip(a, b)]
    ab.sort()
    a = [x for x, y in ab]
    b = [y for x, y in ab]
    sl = SortedList()
    stmax = build_sparse_table(b)
    # print(b)
    # print(query_sparse_table(stmax, 0, len(b) - 1))
    result = 10**20
    for ii, (x, y) in enumerate(list(zip(a, b))):
        biggest = 1
        idx = bisect.bisect(sl, x)
        candidates = []
        for d in range(-1, 2):
            if idx + d >= 0 and idx + d < len(sl):
                candidates.append(sl[idx + d])
        candidates.sort(key=lambda z: abs(x-z))
        biggestother = candidates[0] if ii == len(a)-1 else query_sparse_table(stmax, ii+1, len(b)-1)
        otherbig = max(biggestother, candidates[0] if candidates else -10**20)
        # print(idx, x, y, biggestother, candidates, otherbig)
        result = min(result, abs(x - otherbig))
        sl.add(y)
    print(result)