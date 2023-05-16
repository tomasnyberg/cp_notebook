import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    if nums == list(sorted(nums)):
        print(0)
        continue
    for i in range(len(nums)):
        if nums[i] == i+1:
            print(2)
            break
    else:
        print(1)