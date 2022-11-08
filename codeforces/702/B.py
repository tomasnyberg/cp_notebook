import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    counts = [0]*3
    for x in nums:
        counts[x % 3] += 1
    result = 0
    target = len(nums) // 3
    i = 0
    while counts != [target]*3:
        while counts[i] > target:
            counts[(i+1)%3] += 1
            counts[i] -= 1
            result += 1
        i += 1
        i %= 3
    print(result)