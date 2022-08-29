import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, x = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    nums.sort(key=lambda x: -x)
    taken = 0
    result = 0
    for j in range(len(nums)):
        result += 1 if (taken+1)*nums[j] >= x else 0
        taken = 0 if (taken+1)*nums[j] >= x else taken +1
    print(result)
