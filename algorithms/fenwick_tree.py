class fenwick_tree:
	def __init__(self, values) -> None:
		values.insert(0, 0)
		n = len(values)
		self.tree = values.copy()
		for i in range(1, n):
			parent = i + (i & -i)
			if parent < n: self.tree[parent] += self.tree[i]
	
	def prefixSum(self, i):
		total = 0
		while i != 0:
			total += self.tree[i]
			i &= ~(i&-i)
		return total	
			
	def range_sum(self, left, right):
		assert left <= right, "left is not leq right"
		return self.prefixSum(right) - self.prefixSum(left - 1)
	
	def get(self, i):
		return self.range_sum(i, i)
	
	def add(self, i, val):
		while i < len(self.tree):
			self.tree[i] += val
			i += i & -i
	
	def set(self, i, val):
		self.add(i, val - self.range_sum(i, i))

# examples
#      1 2 3 4 5 6 7
arr = [1,2,3,4,5,6,8]
fwt = fenwick_tree(arr)
print(fwt.range_sum(1, 7))
fwt.set(1, 15)
print(fwt.range_sum(1, 7))
fwt.set(1, 10)
print(fwt.range_sum(1, 7))

fwt.range_sum(5, 2)
