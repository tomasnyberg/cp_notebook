import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, f, k = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    fnum = nums[f-1]
    precounts = nums.count(fnum)
    nums.sort(reverse=True)
    # print(nums)
    nums = nums[k:]
    # print(nums)
    postcounts = nums.count(fnum)
    # print("fnum", fnum)
    # print("k", k, "precounts", precounts, "postcounts", postcounts)
    if postcounts == 0:
        print("YES")
    elif postcounts == precounts:
        print("NO")
    else:
        print("Maybe")
