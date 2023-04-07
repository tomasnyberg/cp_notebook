import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from heapq import heappop, heappush

for i in range(2, len(lines),3):
    a = list(map(int, lines[i].split(" ")))
    b = list(map(int, lines[i+1].split(" ")))
    hq = []
    result = max(a)
    for idx, x in enumerate(a):
        heappush(hq, (-x, idx))
    cost = 0
    while hq and cost < -hq[0][0]:
        result = min(result, -hq[0][0])
        val, idx = heappop(hq)
        cost += b[idx] 
    print(min(result, cost))