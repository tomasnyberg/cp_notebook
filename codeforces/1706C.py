import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    max_cool = math.ceil((len(nums) - 2)/2)
    curr_cool = 0
    for i in range(1, len(nums) - 1):
        if nums[i-1] < nums[i] > nums[i+1]:
            curr_cool+=1
    if curr_cool == max_cool:
        print(0)
        continue
    best = 1000000000000000000
    # If we have an even length, then we can skip ahead once at some point
    dp = [-1]*len(nums)
    for i in range(1, len(nums) - 1):
        leftneeded = 0 if nums[i] > nums[i-1] else nums[i-1] - nums[i] + 1
        rightneeded = 0 if nums[i] > nums[i+1] else nums[i+1] - nums[i] + 1
        dp[i] = max(leftneeded, rightneeded)
    # If we have an odd length, we simply have to take all the odd indexes, otherwise we aren't cool
    if len(nums) % 2 == 1:
        res = 0
        for i in range(1, len(nums)-1,2):
            res += dp[i]
        print(res)
        continue
    print(dp)
    runningsum = 0
    running = []
    for i in range(0, len(nums)):
        if i % 2 == 0 and i != 0:
            runningsum += nums[i]
