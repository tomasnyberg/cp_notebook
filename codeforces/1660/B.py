import sys
from queue import deque
from heapq import heappop, heappush
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    nums.sort()
    dq = deque(nums)
    while len(dq) >= 2:
        a = dq.popleft()
        b = dq.popleft()
        diff = abs(a-b)
        if diff == 0:
            continue
        else:
            dq.append(diff)
    if not dq or dq[0] == 1:
        print("YES")
    else:
        print("NO")
