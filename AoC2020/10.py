import sys
lines = list(map(str.strip, sys.stdin.readlines()))

nums = [0]
for line in lines:
    nums.append(int(line))
nums.sort()
nums.append(nums[-1] + 3)
ones = 0
threes = 0
for i in range(1, len(nums)):
    if nums[i] - nums[i-1] == 1:
        ones += 1
    elif nums[i] - nums[i-1] == 3:
        threes += 1
print(threes, ones)
print(threes * ones)

print(len(nums))
dp = [-1]*len(nums)
def dfs(i):
    if i == len(nums) - 1:
        return 1
    if dp[i] != -1:
        return dp[i]
    total = 0
    idx = i+1
    while idx < len(nums) and nums[idx] - nums[i] <= 3:
        total += dfs(idx)
        idx += 1
    dp[i] = total
    return total

print(dfs(0)) 