import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, x = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    nums.sort()
    mapped = []
    for j in range(len(nums)):
        mapped.append(math.ceil(x /nums[j]))
    result = 0
    dp = [0]*len(nums)
    for j in range(len(nums)-1,-1,-1):
        dp[j] = 1 if j + mapped[j] <= len(nums) else 0
        if j + mapped[j] < len(nums):
            dp[j] += dp[j + mapped[j]] 
    print(max(dp))
        # if 