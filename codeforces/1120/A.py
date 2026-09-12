import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    while len(nums) > 1:
        for turn in [1,0]:
            if len(nums) == 1:
                break
            for i in range(1, len(nums)):
                if nums[i]+nums[i-1] == 1:
                    nums[i] = turn
                    nums.pop(i-1)
                    break
            else:
                nums.pop()
    print("Bessie" if nums[0] == 1 else "Elsie")


