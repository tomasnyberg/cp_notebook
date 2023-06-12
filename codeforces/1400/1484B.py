import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if len(nums) == 1 or all([x == nums[0] for x in nums]):
        print(0)
        continue
    if all([nums[i] - nums[i+1] == 1 for i in range(len(nums) - 1)]):
        print(0)
        continue
    # We can't have two decreasing in a row unless their diff is 1 and c == m-1
    # if for any index i, 1 <= i < len(nums) - 1, we have nums[i-1] > nums[i] > nums[i+1]
    # our answer is -1
    #unless their diff is 1 and c == m-1
    c = -1
    mod = -1
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            c = nums[i+1] - nums[i]
            break
    bad = False
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i+1] and nums[i+1] - nums[i] != c:
            bad = True
            break
        if nums[i] > nums[i+1]:
            mod = nums[i] + c - nums[i+1]
            break
    if all([nums[i] < nums[i+1] for i in range(len(nums) - 1)]):
        print(0)
        continue
    if bad:
        print(-1)
        continue
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            if nums[i] + c - nums[i+1] != mod:
                bad = True
                break
    # print("MOD", mod)
    if bad or mod <= max(nums):
        print(-1)
        continue
    print(mod, c)



