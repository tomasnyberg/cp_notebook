import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def update(index, value, array, bi_tree):
	while index < len(array):
		bi_tree[index] += value
		index += index & -index

def get_sum(index, bi_tree):
	ans = 0
	while index > 0:
		ans += bi_tree[index]
		index -= index & -index
	return ans

def get_range_sum(left, right, bi_tree):
	ans = get_sum(right, bi_tree) - get_sum(left - 1, bi_tree)
	return ans

n, q = map(int, lines[0].split(" "))

freecols = [0] + [i for i in range(1, n+1)]
freerows = [0] + [i for i in range(1, n+1)]
colcounter = [0 for i in range(n+1)]
rowcounter = [0 for i in range(n+1)]

freecolsbit = [0 for i in range(n+1)]
freerowsbit = [0 for i in range(n+1)]

for index in range(1, n+1):
    update(index, freerows[index], freerows, freerowsbit)

for index in range(1, n+1):
    update(index, freecols[index], freecols, freecolsbit)
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
                update(x, 0-freerows[x], freerows, freerowsbit)
            rowcounter[x] +=1
            if colcounter[y] == 0:
                update(y, 0-freecols[y], freecols, freecolsbit)
            colcounter[y] +=1
        else:
            # remove an existing rook, if we no longer have one in that row we
            # reset the value in our fenwick tree, to indicate that that one is now free
            if rowcounter[x] == 1:
                update(x, x-freerows[x], freerows, freerowsbit)
            rowcounter[x] -=1
            if colcounter[y] == 1:
                update(y, y-freecols[y], freecols, freecolsbit)
            colcounter[y] -=1
        continue
    x1, y1, x2, y2 = query[1:]
    print(x1, x2, y1, y2)
    print(get_range_sum(x1,x2, freerowsbit))
    print(get_range_sum(y1, y2, freecolsbit))
    print()
    rowgood = get_range_sum(x1, x2, freerowsbit) == 0
    colgood = get_range_sum(y1, y2, freecolsbit) == 0
    # print("YES" if rowgood or colgood else "NO")