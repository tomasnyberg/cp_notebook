import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))

class fenwick_tree:
	def __init__(self, values) -> None:
		values.insert(0, 0)
		n = len(values)
		self.n = n
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

	def dbg(self):
		for i in range(1, self.n):
			print(self.get(i), end=', ')
		print()

# TODO Remember to add int wrapping if using dict

# k = 2
# [1, 2, 3, 4]
#     A  B
# [1, 2, 4]
#     A
#     B
# [1, 4]
#  B  A

# is greedy always best.... ? 

def find_index(fwt, fake_idx):
    low = 0
    high = fwt.n
    while low < high:
        mid = (low+high) >> 1
        if fwt.prefixSum(mid) > fake_idx:
            high = mid
        else:
            low = mid + 1
    return low - 1

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split())
    nums = list(map(int, lines[i+1].split()))
    fwt = fenwick_tree([1]*n)
    result = 0
    while n >= k:
        a_idx = find_index(fwt, k-1)
        b_idx = find_index(fwt, n-k)
        ascore = nums[a_idx]
        bscore = nums[b_idx]
        if ascore>=bscore:
            nums[a_idx] = 0
            fwt.set(a_idx+1, 0)
            result += ascore
        else:
            nums[b_idx] = 0
            fwt.set(b_idx+1, 0)
            result += bscore
        # fwt.dbg()
        # print(nums)
        # print()
        n-=1
    print(result)
