import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    nums = [x - 1 for x in nums]
    n = len(nums)
    curr = [0]*n
    curr[nums[0]] = 1
    for idx in nums[1:]:
        for d in [-1, 1]:
            if 0 <= idx + d < n and curr[idx+d]:
                curr[idx] = 1
                break
        else:
            print("NO")
            break
    else:
        print("YES")


