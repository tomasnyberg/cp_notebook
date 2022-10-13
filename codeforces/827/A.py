import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    nums = list(map(int, line.split(" ")))
    if nums[0] == nums[1] + nums[2] or nums[1] == nums[0] + nums[2] or nums[2] == nums[0] + nums[1]:
        print("YES")
    else:
        print("NO")