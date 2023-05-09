import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from heapq import heappop, heappush

nums = list(map(int, lines[1].split(" ")))
health = 0
hq = []
for x in nums:
    if health + x >= 0:
        heappush(hq, x)
        health += x
    elif hq:
        if x > hq[0]:
            prev = heappop(hq)
            heappush(hq, x)
            health += x - prev
print(len(hq))
