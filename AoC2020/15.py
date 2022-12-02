import sys
lines = list(map(str.strip, sys.stdin.readlines()))

said = {}

nums = list(map(int, lines[0].split(",")))
for idx, x in enumerate(nums):
    said[x] = [idx]

for i in range(30000000 - len(nums)):
    if i % 100000 == 0:
        print(i)
    prev = nums[-1]
    if len(said[prev]) == 1:
        nums.append(0)
        if 0 not in said:
            said[0] = []
        said[0].append(len(nums) - 1)
    else:
        nums.append(said[prev][-1] - said[prev][-2])
        if nums[-1] not in said:
            said[nums[-1]] = [len(nums) - 1]
        else:
            said[nums[-1]].append(len(nums)-1)

print(nums[-5:])
