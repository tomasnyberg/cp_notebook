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

sl = SortedList()
sl.add(5)
sl.add(2)
sl.add(7)
sl.add(10)
sl.add(9)
print(sl[0])