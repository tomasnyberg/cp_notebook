import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    nums.sort()
    bad = False
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i+1]:
            bad = True
            break
    print("NO" if bad else "YES")