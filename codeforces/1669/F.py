import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    CS_left = cum_sum(nums)
    CS_right = cum_sum(list(reversed(nums)))
    CSR_indexes = {}
    for idx, x in enumerate(CS_right):
        CSR_indexes[x] = (len(nums) - 1 - idx, idx)
    most = -1
    for idx, x in enumerate(CS_left):
        if x in CSR_indexes and CSR_indexes[x][0] >= idx + 1:
            most = CSR_indexes[x][1] + idx + 2
    if most == -1:
        print(0)
    else:
        print(most)