import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    nums.sort()
    nums = deque(nums)
    result = 0
    while len(nums) > 1:
        result += nums.pop() - nums.popleft()
    print(result)
        
