import sys
import bisect
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    cands = []
    for idx, num in enumerate(nums):
        if idx + 1 > num:
            cands.append(idx + 1)
    result = 0 
    for idx, num in enumerate(nums):
        if idx + 1 > num:
            result += bisect.bisect_left(cands, num)
    print(result)