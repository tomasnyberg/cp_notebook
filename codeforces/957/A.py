import sys
if sys.argv[-1] == "--debug":
    sys.stdin = open("in")
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    nums = list(map(int, line.split()))
    for _ in range(5):
        smallestidx = nums.index(min(nums))
        nums[smallestidx] += 1
    print(nums[0] * nums[1] * nums[2])
