import math
from collections import deque
import sys
lines = list(map(str.strip, sys.stdin.readlines()))


def cum_sum(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result

# lines = """1
# 5 7
# 1 4 1 1 1""".split("\n")

for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    total = sum(nums)
    if total <= k:
        print(0)
        continue
    nums.sort()
    CS = cum_sum(nums)
    result = 10**25
    for y in range(n):
        # Maybe ceil
        x = math.floor((k - CS[n-1-y] + CS[0])/(y + 1))
        x = min(x, nums[0])
        diff = nums[0] - x
        result = min(y + diff, result)
    print(result)
