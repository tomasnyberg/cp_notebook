import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    # replace all 1s with 2s
    nums = list(map(lambda x: 2 if x == 1 else x, nums))
    for i in range(1, len(nums)):
        if nums[i] % nums[i-1] == 0:
            nums[i] += 1
    print(*nums)
        