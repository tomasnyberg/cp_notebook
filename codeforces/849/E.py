import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    smallestnegative = -10**9
    negatives = 0
    for num in nums:
        if num <= 0:
            negatives += 1
            smallestnegative = max(smallestnegative, num)
    if negatives % 2 == 0:
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        print(sum(nums))
    else:
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        print(sum(nums) - 2*abs(smallestnegative))