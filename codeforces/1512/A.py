import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    count = {}
    for x in nums:
        count[x] = 1 if x not in count else count[x] + 1
    for idx, x in enumerate(nums):
        if count[x] == 1:
            print(idx + 1)
            break