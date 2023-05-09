import sys
lines = list(map(str.strip, sys.stdin.readlines()))

nums = list(map(int, lines[1].split(" ")))
dp = [[-10**10] * (len(nums) + 1) for _ in range(len(nums) + 1)]
dp[0][0] = 0

for i in range(1, len(nums) + 1):
    curr_potion = nums[i - 1]
    for j in range(len(nums) + 1):
        if dp[i-1][j-1] + curr_potion >= 0:
            dp[i][j] = max(dp[i-1][j-1] + curr_potion, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]


# for i, xs in enumerate(dp):
#     if i > 0:
#         print("Curr:", nums[i-1])
#     for x in xs:
#         print(x if x != -10**10 else "x", end=" ")
#     print()
            
result = 0
for i in range(len(dp[0])):
    if dp[-1][i] >= 0:
        result = i
print(result)






