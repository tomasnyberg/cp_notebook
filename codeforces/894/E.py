import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache
from heapq import heappop, heappush
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, m, d = list(map(int, lines[ii].split()))
    nums = list(map(int, lines[ii+1].split()))
    hq = []
    heapsum = 0
    result = 0
    for i, x in enumerate(nums):
        if x > 0:
            heapsum += x
            heappush(hq, x)
        if len(hq) > m:
            heapsum -= heappop(hq)
        result = max(result, heapsum - (i+1)*d)
    print(result)
            
