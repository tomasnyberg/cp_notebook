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
        print(sum(dp[1:-1:2]))
        continue
    sum_at_even_indexes = sum([x for x in dp[2::2]])
    even_indexes = [0]*len(nums)
    for i in range(1, len(nums) - 1):
        if i % 2 == 0:
            even_indexes[i] = sum_at_even_indexes
            sum_at_even_indexes -= dp[i]
    running_odd = 0
    best = 100000000000000000
    for i in range(1, len(dp) - 1, 2):
        best = min(running_odd + even_indexes[i+1], best)
        running_odd += dp[i]
    print(min(best, running_odd))