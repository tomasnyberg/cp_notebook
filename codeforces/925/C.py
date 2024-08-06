import sys
from collections import Counter
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if all(x == nums[0] for x in nums):
        print(0)
        continue
    left_prefix = {}
    for x in nums:
        if not left_prefix:
            left_prefix[x] = 1
        else:
            if left_prefix.get(x, 0) == 0:
                break
            left_prefix[x] += 1
    right_prefix = {}
    for x in nums[::-1]:
        if not right_prefix:
            right_prefix[x] = 1
        else:
            if right_prefix.get(x, 0) == 0:
                break
            right_prefix[x] += 1
    result = 10**9
    for x in set(nums):
        result = min(result, len(nums) - left_prefix.get(x, 0) -
                     right_prefix.get(x, 0))
    print(result)
