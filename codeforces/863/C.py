import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    original = nums[:]
    firstsmaller = -1
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            firstsmaller = i
            nums.insert(i+1, 0)
            break
    else:
        nums.append(nums[-1])
        print(*nums)
        continue
    for i in range(len(original)):
        this = max(nums[i], nums[i+1])
        if this != original[i]:
            nums[i] = nums[i+1]
    print(*nums)
    

    