import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    nums = list(filter(lambda x: x != 0, nums))
    streak = 0
    result = 0
    result2 = 0
    for num in nums:
        if num <= 0:
            streak = 1
        else:
            result += streak
            streak = 0
        result2 += abs(num)
    print(result2, result + streak)

