import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    
    dp = [[0, 0] for _ in range(len(nums) + 2)]
    
    for i in range(len(nums)-1, -1, -1):
        dp[i][0] = min(dp[i+1][1], dp[i+2][1])
        dp[i][1] = min(dp[i+1][0] + nums[i], dp[i+2][0] + nums[i] + (nums[i+1] if i+1 < len(nums) else 0))
        
    print(dp[0][1])