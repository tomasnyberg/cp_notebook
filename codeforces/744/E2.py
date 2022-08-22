import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from queue import deque
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

def merge_sort(xs, result):
    def merge(left, right, result):
        a = 0
        b = 0
        merged = []
        while a < len(left) or b < len(right):
            if a == len(left) or b == len(right):
                merged += left[a:]
                merged += right[b:]
                break
            if left[a] <= right[b]:
                merged.append(left[a])  
                a += 1
            else:
                merged.append(right[b])
                b += 1
                result[0] += len(left) - a
        return merged
    if len(xs) == 1:
        return xs
    n = len(xs)
    return merge(merge_sort(xs[:n//2], result), merge_sort(xs[n//2:], result), result)

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    numscopy = list(sorted(nums.copy()))
    indexes = {}
    for idx, x in enumerate(numscopy):
        if x not in indexes:
            indexes[x] = idx
        indexes[x] = idx
    fwt = fenwick_tree([0]*len(nums))
    dq = deque()
    
    for x in nums:
        #Calculate the number of elements < x using the FWT
        lessthan = fwt.prefixSum(indexes[x]+1)
        greaterthan = fwt.range_sum(indexes[x] + 1, len(nums))
        # print(dq)
        # print(x, "has", lessthan, "elements that are less than it ")
        if lessthan <= greaterthan:
            dq.appendleft(x)
        else:
            dq.append(x)
        fwt.add(indexes[x]+1, 1)
    # print(dq)
    nums = list(dq)
    result = [0]
    merge_sort(nums, result)
    print(result[0])
