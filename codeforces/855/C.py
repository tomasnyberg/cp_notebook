import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque
from heapq import heappush, heappop

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    hq = []
    result = 0
    for i in range(len(nums)):
        if not nums[i]:
            if hq:
                result += -heappop(hq)
        else:
            heappush(hq, -nums[i])
    print(result)

    
        

