import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from heapq import heappush, heappop

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    hq = []
    for idx, x in enumerate(nums):
        heappush(hq, [-x, idx])
    talks = []
    while len(hq) >= 2:
        atalksleft, aindex = heappop(hq)
        btalksleft, bindex = heappop(hq)
        if not atalksleft or not btalksleft: break
        atalksleft+=1
        btalksleft+=1
        talks.append([aindex, bindex])
        if atalksleft:
            heappush(hq, [atalksleft, aindex])
        if btalksleft:
            heappush(hq, [btalksleft, bindex])
    print(len(talks))
    for a, b in talks:
        print(a+1,b+1)