import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if len(nums) == 2:
        print("YES" if nums[0] <= nums[1] else "NO")
        continue
    for i in range(1, len(nums) - 1):
        if nums[i-1] > nums[i] < nums[i+1]:
            print("NO")
            break
    else:
        print("YES")