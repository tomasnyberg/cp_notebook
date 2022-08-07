import sys
from queue import deque
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

n, m = map(int, lines[0].split(" "))
matrix = []
for line in lines[1:]:
    matrix.append(list(map(int, line.split(" "))))
rowoccurrences = {} # Color : [] occurrences
coloccurrences = {} # Color : [] occurrences
for i in range(n):
    for j in range(m):
        val = matrix[i][j]
        if val not in rowoccurrences: rowoccurrences[val] = []
        if val not in coloccurrences: coloccurrences[val] = []
        rowoccurrences[val].append(i)
        coloccurrences[val].append(j)

# print(rowoccurrences)
result = 0
for color in rowoccurrences:
    arr = rowoccurrences[color]
    arr.sort()
    cumsum = cum_sum(arr)
    for i in range(0, len(arr)-1):
        result += cumsum[-1] - cumsum[i] - (len(arr)-1-i)*arr[i]

for color in coloccurrences:
    arr = coloccurrences[color]
    arr.sort()
    cumsum = cum_sum(arr)
    for i in range(0, len(arr)-1):
        result += cumsum[-1] - cumsum[i] - (len(arr)-1-i)*arr[i]
print(result)

