import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    nums = list(map(int, line.split(" ")))
    res = [nums[0], nums[1]]
    if nums[2] == nums[0] + nums[1]:
        res.append(nums[3])
    else:
        res.append(nums[2])
    print(*res)

