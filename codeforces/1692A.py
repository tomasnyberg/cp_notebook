import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    nums = list(map(int, line.split(" ")))
    count = 0
    for num in nums[1:]:
        if num > nums[0]:
            count += 1
    print(count)
