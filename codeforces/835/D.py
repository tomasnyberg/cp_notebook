import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    increasing = False
    bad = False
    for i in range(len(nums)-1):
        if nums[i+1] > nums[i] and not increasing:
            increasing = True
        if nums[i+1] < nums[i] and increasing:
            bad = True
            break
    print("NO" if bad else "YES")


