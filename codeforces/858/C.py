import sys
import itertools
lines = list(map(str.strip, sys.stdin.readlines()))

good_len_4 = [[-1, -1, -1, 2],
[2, 2, 2, 2],
[0, 0, 0, 0]]

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if len(nums) == 2:
        print(max(nums) - min(nums))
        continue
    if len(nums) == 4:
        nums.sort()
        res = 10**25
        for good in good_len_4:
            good.sort()
            # print(nums, good, sum(abs(x-y) for x,y in zip(nums, good)))
            res = min(res, sum(abs(x-y) for x,y in zip(nums, good)))
        # Find the number closest to 2 in the array
        print(res)
        continue
    else:
        # Print the sum of the absolute values of x
        total = 0
        for x in nums:
            total += abs(x)
        print(max(0, total - 3))
        
