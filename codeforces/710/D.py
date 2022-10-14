from collections import deque
from heapq import heappop, heappush
import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    counts = {}
    for x in nums:
        counts[x] = 1 if x not in counts else counts[x] + 1
    biggest = max([counts[key] for key in counts])
    totalwob = sum([counts[key] for key in counts]) - biggest
    bmt = biggest - totalwob
    print(bmt if bmt > 0 else (1 if len(nums) % 2 == 1 else 0))
