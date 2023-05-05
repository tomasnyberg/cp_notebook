import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    result = 0
    streak = 0
    for x in nums:
        if x == 0:
            streak += 1
            result = max(result, streak)
        else:
            streak = 0
    result = max(result, streak)
    print(result)