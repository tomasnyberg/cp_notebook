import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    nums = list(map(lambda x: ord(x) - 97, line))
    length = len(nums)
    decreasing = nums[0] >= nums[-1]
    for i in range(len(nums)):
        nums[i] = [nums[i], i+1]
    if decreasing:
        nums = list(filter(lambda x: x[0] <= nums[0][0] and x[0] >= nums[-1][0], nums))
    else:
        nums = list(filter(lambda x: x[0] >= nums[0][0] and x[0] <= nums[-1][0], nums))
    shortnums = nums[1:-1]
    shortnums.sort(key=lambda x: abs(x[0]-nums[0][0]))
    # print(shortnums)
    result = [1]
    totalcost = abs(nums[0][0] - nums[-1][0])
    for _, index in shortnums:
        result.append(index)
    result.append(length)
    print(abs(nums[0][0]-nums[-1][0]), len(result))
    print(*result)

