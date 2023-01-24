import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    one_count = nums.count(1)
    result = len(nums)
    result -= one_count//2
    print(result)