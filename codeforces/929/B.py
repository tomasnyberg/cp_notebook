import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    mods = [[], [], []]
    tot = sum(nums)
    for x in nums:
        mods[x % 3].append(x)
    if tot % 3 == 0:
        print(0)
    if tot % 3 == 1:
        if len(mods[1]) >= 1:
            print(1)
        else:
            print(min(2, len(nums)))
    if tot % 3 == 2:
        print(1)
