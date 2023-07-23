import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from math import ceil
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if nums != list(sorted(nums)):
        print("0")
        continue
    result = 10**12
    for i in range(len(nums)):
        before = -10**12 if i == 0 else nums[i-1]
        after = 10**12 if i == len(nums)-1 else nums[i+1]
        take_away = ceil((nums[i] - before + 1) / 2)
        add = ceil((after - nums[i] + 1) / 2)
        result = min(result, take_away, add)
    print(result)