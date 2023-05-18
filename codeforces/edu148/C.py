import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    if len(nums) == 1:
        print(1)
        continue
    contrast = sum([abs(nums[i] - nums[i-1]) for i in range(1, len(nums))])
    if contrast == 0:
        print(1)
        continue
    start = 1
    while start < len(nums) and nums[start] == nums[0]:
        start += 1
    increasing = nums[start] >= nums[0]
    # print(nums, start)
    result = 2
    for i in range(start, len(nums)):
        if increasing:
            if nums[i] < nums[i-1]:
                increasing = False
                result += 1
        else:
            if nums[i] > nums[i-1]:
                increasing = True
                result += 1
    print(result)
    