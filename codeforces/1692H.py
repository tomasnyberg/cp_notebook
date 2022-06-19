import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    uniques = set(nums)
    best_unique = -1
    biggest_unique = -1
    best_started = -1
    best_ended = -1
    consecutive = {}
    for idx, num in enumerate(nums):
        if num not in consecutive:
            consecutive[num] = [0, idx]
        consecutive[num][0] += 1
        if consecutive[num][0] > biggest_unique:
            best_started = consecutive[num][1]
            best_ended = idx
            biggest_unique = consecutive[num][0]
            best_unique = num
        to_del = []
        for x in consecutive:
            if x != num:
                if consecutive[x][0] - 1 == 0:
                    to_del.append(x)
                else:
                    consecutive[x][0] = max(consecutive[x][0] - 1, 0)
        for td in to_del:
            del consecutive[td]
    print(best_unique, best_started+1, best_ended+1)
    # Find the best unique, then we can do this
    # biggest = 0
    # biggest_dp = []
    # dp = [1 if nums[0] == best_unique else -1]
    # for i in range(1, len(nums)):
    #     match = 1 if nums[i] == best_unique else -1
    #     dp.append(max(dp[i-1] + match, match))
    # if max(dp) > biggest:
    #     biggest = max(dp)
    #     biggest_dp = dp
    # idx = biggest_dp.index(biggest)
    # right = idx
    # while idx > 0 and biggest_dp[idx-1] >= 0:
    #     idx -= 1
    # print(best_unique, idx+1, right+1) 
    