import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    nums.sort()
    candidates = []
    best = (10**10, -1)
    for i in range(len(nums) - 1):
        d = nums[i+1] - nums[i]
        if d < best[0]:
            best = (d, i)
    _, start = best
    print(*([nums[start]] + nums[start + 2:] + nums[:start] + [nums[start + 1]]))
    