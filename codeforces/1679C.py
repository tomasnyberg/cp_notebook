import sys
lines = list(map(str.strip, sys.stdin.readlines()))

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

n, q = map(int, lines[0].split(" "))

freecols = [i for i in range(1, n+1)]
freerows = [i for i in range(1, n+1)]
colcounter = [0 for i in range(n+1)]
rowcounter = [0 for i in range(n+1)]

col_fwt = fenwick_tree(freecols)
row_fwt = fenwick_tree(freerows)


# [1,3,6,10,15,21,28,36]
# [1,2,3,4,5,6,7,8]
# update(3, 0-freecols[3], freecols, freecolsbit)
# print(get_range_sum(2, 6, freecolsbit))
for i in range(1, len(lines)):
    query = list(map(int, lines[i].split(" ")))
    if query[0] == 1 or query[0] == 2:
        x, y = query[1:]
        if query[0] == 1:
            # Add a new rook, if we didn't have one in that row before we set the value
            # in our fenwick tree for that index to be 0
            if rowcounter[x] == 0:
                row_fwt.set(x, 0)
            rowcounter[x] +=1
            if colcounter[y] == 0:
                col_fwt.set(y, 0)
            colcounter[y] +=1
        else:
            # remove an existing rook, if we no longer have one in that row we
            # reset the value in our fenwick tree, to indicate that that one is now free
            if rowcounter[x] == 1:
                row_fwt.set(x, x)
            rowcounter[x] -=1
            if colcounter[y] == 1:
                col_fwt.set(y, y)
            colcounter[y] -=1
        continue
    x1, y1, x2, y2 = query[1:]
    a = row_fwt.range_sum(x1,x2) == 0
    b = col_fwt.range_sum(y1, y2) == 0
    print("YES" if a or b else "NO")