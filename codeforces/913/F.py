import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

# lines = ["", "", "3 7 10 5"]

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if nums == list(sorted(nums)):
        print(0)
        continue
    smallest = min(nums)
    smallestseen = False
    forwardstart = -1
    for i in range(len(nums) - 1, -1,-1):
        if nums[i] != smallest and smallestseen:
            break
        if nums[i] == smallest:
            smallestseen = True
            forwardstart = i
    backwardstart = -1
    smallestseen = False
    for i in range(len(nums)):
        if nums[i] != smallest and smallestseen:
            break
        if nums[i] == smallest:
            smallestseen = True
            backwardstart = i
    forward = True
    backward = True
    for i in range(1, len(nums)):
        idx = (forwardstart + i) % len(nums)
        prev = (idx - 1) % len(nums)
        if nums[idx] < nums[prev]:
            forward = False
            break
    for i in range(1, len(nums)):
        idx = (backwardstart - i) % len(nums)
        prev = (idx + 1) % len(nums)
        if nums[idx] < nums[prev]:
            backward = False
            break
    if not forward and not backward:
        print(-1)
        continue
    result = 10**9
    if backward:
        popendandreverse = len(nums) - backwardstart - 1 + 1
        reverseandpop = 1 + backwardstart + 1
        result = min(result, popendandreverse, reverseandpop)
    if forward:
        popend = len(nums) - forwardstart
        reverseandpopandreverse = 1 + (forwardstart) + 1
        result = min(result, popend, reverseandpopandreverse)
    print(result)


    
     
        