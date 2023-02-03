import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    for i in range(1, len(nums)):
        a = nums[i]
        b = nums[i-1]
        if -a + (-b) > a + b:
            nums[i] = -a
            nums[i-1] = -b
    print(sum(nums))