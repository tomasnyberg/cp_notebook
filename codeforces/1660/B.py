import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(2, len(lines), 2):
    nums = list(map(int, lines[i].split(" ")))
    nums.sort(key=lambda x: -x)
    bad = False
    if len(nums) == 1:
        if nums[0] > 1:
            print("NO")
        else:
            print("YES")
        continue
    for i in range(0, len(nums), 2):
        if i == len(nums) - 1: break
        if nums[i] - nums[i+1] > 1 and i == 0:
            bad = True
            break
    print("NO" if bad else "YES")


