import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    result = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] >= nums[i-1]:
            result.append(nums[i])
        else:
            result.append(1)
            result.append(nums[i])
    print(len(result))
    print(*result)
