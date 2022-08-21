import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from queue import deque

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    dq = deque([])
    for x in nums:
        if not dq or x < dq[0]:
            dq.appendleft(x)
        else:
            dq.append(x)
    for x in dq:
        print(x, end=" ")
    print()