import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    for i in range(len(nums) - 1, 0, -2):
        if nums[i] < nums[i-1]:
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp
    print("YES" if nums == list(sorted(nums)) else "NO")