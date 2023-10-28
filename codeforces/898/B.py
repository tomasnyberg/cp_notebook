import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    nums.sort()
    nums[0] += 1
    result = 1
    for x in nums:
        result *= x
    print(result)