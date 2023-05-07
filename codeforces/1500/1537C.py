import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    nums.sort()
    candidates = []
    smallestdiff = 10**10
    for i in range(len(nums) - 1):
        smallestdiff = min(smallestdiff, nums[i+1] - nums[i])
    best = (0, -1)
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] != smallestdiff: continue
        right = len(nums) - (i+1)
        left = i
        if right + left > best[0]:\
            best = (right + left, i)
    _, start = best
    print(*([nums[start]] + nums[start + 2:] + nums[:start] + [nums[start + 1]]))
    