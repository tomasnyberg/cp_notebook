import sys
lines = list(map(str.strip, sys.stdin.readlines()))


for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    dp = [0]*len(nums)
    result = 0
    for i in range(len(nums)-1,-1,-1):
        to_add = dp[i+nums[i]] if i+nums[i] < len(nums) else 0
        dp[i] = nums[i] + to_add
    print(max(dp))
