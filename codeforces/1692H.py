import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    uniques = set(nums)
    best_unique = -1
    best_consecutive = {}
    consecutive = {}
    for num in nums:
        if num not in consecutive:
            consecutive[num] = 0
        consecutive[num] += 1
        if num not in best_consecutive:
            best_consecutive[num] = 0
        best_consecutive[num] = max(consecutive[num], best_consecutive[num])
        to_del = []
        for x in consecutive:
            if x != num:
                if consecutive[x] - 1 == 0:
                    to_del.append(x)
                else:
                    consecutive[x] = max(consecutive[x] - 1, 0)
        for td in to_del:
            del consecutive[td]
    BIG = -1
    for k in best_consecutive:
        if best_consecutive[k] > BIG:
            best_unique = k
            BIG = best_consecutive[k]
    # Find the best unique, then we can do this
    biggest = 0
    biggest_dp = []
    dp = [1 if nums[0] == best_unique else -1]
    for i in range(1, len(nums)):
        match = 1 if nums[i] == best_unique else -1
        dp.append(max(dp[i-1] + match, match))
    if max(dp) > biggest:
        biggest = max(dp)
        biggest_dp = dp
    idx = biggest_dp.index(biggest)
    right = idx
    while idx > 0 and biggest_dp[idx-1] >= 0:
        idx -= 1
    print(best_unique, idx+1, right+1) 
    