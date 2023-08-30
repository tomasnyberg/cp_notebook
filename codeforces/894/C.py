import sys
from bisect import bisect_right
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    nums += [0]
    horizontal = []
    broken = False
    for i, x in enumerate(nums):
        if i == len(nums) - 1:
            horizontal.append(i+1)
            continue
        while x > nums[i+1]:
            horizontal.append(i+1)
            if len(horizontal) >= len(nums):
                broken = True
                break
            x-=1
        if broken:
            break
    if broken:
        print("NO")
        continue
    print("YES" if horizontal[:-1][::-1] == nums[:-1] else "NO")
