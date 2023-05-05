import sys
lines = list(map(str.strip, sys.stdin.readlines()))

rowsize = 1
rows = []
curr_row = []
places = {}
for i in range(1, (2023*(2023+1)) // 2 + 2):
    if len(curr_row) == rowsize:
        rows.append(curr_row)
        curr_row = []
        rowsize+=1
    places[i] = (len(rows), len(curr_row))
    curr_row.append(i**2)

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result
for i in range(len(rows)):
    rows[i] = cum_sum(rows[i])

# print(rows[-1])
for line in lines[1:]:
    n = int(line)
    i, j = places[n]
    left = j
    right = j
    result = 0
    while i >= 0:
        result += rows[i][right] - (rows[i][left-1] if left > 0 else 0)
        i -= 1
        if i < 0: break
        left -= 1
        left = max(left, 0)
        right = min(right, len(rows[i])-1)
    print(result)


