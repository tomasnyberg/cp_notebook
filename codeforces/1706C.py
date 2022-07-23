import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    max_cool = math.ceil((len(nums) - 2)/2)
    curr_cool = 0
    for i in range(1, len(nums) - 1):
        if nums[i-1] < nums[i] > nums[i+1]:
            curr_cool+=1
    if curr_cool == max_cool:
        print(0)
        continue
    best = 1000000000000000000
    # If we have an even len nums, then we can check both even and odd indexes
    if len(nums) % 2 == 0:
        cost = 0
        for i in range(2, len(nums) - 1, 2):
            leftcost = 0 if nums[i] > nums[i-1] else nums[i-1] - nums[i] + 1
            rightcost = 0 if nums[i] > nums[i+1] else nums[i+1] - nums[i] + 1
            cost += max(leftcost, rightcost)
        best = cost
    cost = 0
    for i in range(1, len(nums) - 1, 2):
        leftcost = 0 if nums[i] > nums[i-1] else nums[i-1] - nums[i] + 1
        rightcost = 0 if nums[i] > nums[i+1] else nums[i+1] - nums[i] + 1
        cost += max(leftcost, rightcost)
    best = min(cost, best)
    print(best)


