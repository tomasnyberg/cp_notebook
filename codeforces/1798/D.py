import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    nums.sort()
    target = nums[-1] - nums[0]
    dq = deque(nums)
    xs = []
    running = 0
    good = True
    while dq:
        if running + dq[-1] < target:
            xs.append(dq.pop())
        else:
            xs.append(dq.popleft())
        running += xs[-1]
        if abs(running) >= target:
            good = False
            break
    if good:
        print("Yes")
        print(*xs)
    else:
        print("No")
     
    
