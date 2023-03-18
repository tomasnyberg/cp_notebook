import sys
from collections import deque
lines = list(map(str.strip, sys.stdin.readlines()))

def get_MEX(nums):
    nums = set(nums)
    for i in range(len(nums) + 1):
        if i not in nums:
            return i

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
    zeroes = counts.get(0, 0)
    nonzeroes = len(nums) - zeroes
    if zeroes - 1 <= nonzeroes:
        print(0)
        continue
    for i in range(1, len(nums) + 1):
        if i not in counts or nonzeroes - counts[i] > 0:
            print(i)
            break
    