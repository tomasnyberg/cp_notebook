import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from heapq import heappop, heappush

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    left = 0
    right = 0
    while right < len(nums):
        right += 1
        while nums[left] < (right - left):
            left += 1
        print(right - left, end=' ')
    print()