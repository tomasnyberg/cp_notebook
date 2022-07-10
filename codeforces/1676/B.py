import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    small = min(nums)
    result = 0
    for x in nums:
        result += x - small
    print(result)