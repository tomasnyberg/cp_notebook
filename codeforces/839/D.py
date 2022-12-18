import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if nums == sorted(nums):
        print(0)
    elif nums == sorted(nums, reverse=True):
        print(nums[0])
    elif len(set(nums)) == 2:
        parity = nums[0] % 2
        if all([x % 2 == parity for x in nums]):
            a = nums[0]
            b = (set(nums) - {a}).pop()
            print(math.ceil((a + b) / 2))
        else:
            print(-1)
    elif nums[:-1] == sorted(nums[:-1]):
        candidate = math.ceil((nums[-2] + nums[-1]) / 2)
        for i in range(len(nums)):
            nums[i] = abs(nums[i] - candidate)
        if nums == sorted(nums):
            print(candidate)
        else:
            print(-1)
    elif nums[1:] == sorted(nums[1:]):
        candidate = math.ceil((nums[0] + nums[1]) / 2)
        for i in range(len(nums)):
            nums[i] = abs(nums[i] - candidate)
        if nums == sorted(nums):
            print(candidate)
        else:
            print(-1)
    else:
        print(-1)