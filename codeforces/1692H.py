import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    uniques = set(nums)
    biggest = 0
    biggest_dp = []
    best_unique = -1
    for unique in uniques:
        dp = [1 if nums[0] == unique else -1]
        for i in range(1, len(nums)):
            match = 1 if nums[i] == unique else -1
            dp.append(max(dp[i-1] + match, match))
        if max(dp) > biggest:
            biggest = max(dp)
            biggest_dp = dp
            best_unique = unique
    idx = biggest_dp.index(biggest)
    right = idx
    while idx > 0 and biggest_dp[idx-1] >= 0:
        idx -= 1
    print(best_unique, idx+1, right+1) 
    