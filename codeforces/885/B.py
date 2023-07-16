import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    indices = {}
    for idx, x in enumerate(nums):
        if x not in indices:
            indices[x] = []
        indices[x].append(idx)
    for key in indices:
        indices[key].append(len(nums))
    result = len(nums)
    for x in indices:
        steps = []
        prev = -1
        for y in indices[x]:
            steps.append(y - prev - 1)
            prev = y
        steps.sort()
        steps[-1] //= 2
        result = min(result, max(steps))
    print(result)


