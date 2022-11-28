import sys
lines = list(map(str.strip, sys.stdin.readlines()))

nums = [0]
for line in lines:
    nums.append(int(line))
nums.sort()
nums.append(nums[-1] + 3)

def part_one():
    counts = {0: 0, 1: 0, 2:0, 3:0}
    for i in range(1, len(nums)):
        counts[nums[i] - nums[i-1]] +=1
    return (counts[3] * counts[1])

def part_two():
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
    return dfs(0)

print("Part one:", part_one())
print("Part two:", part_two())
