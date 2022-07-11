import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(2, len(lines), 2):
    nums = list(map(int, lines[i].split(" ")))
    nums.sort(key=lambda x: -x)
    if len(nums) == 1: print("YES") if nums[0] == 1 else print("NO")
    else: print("NO") if nums[0] - nums[1] > 1 else print("YES")


