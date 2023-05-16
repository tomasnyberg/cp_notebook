import sys
from math import ceil
lines = list(map(str.strip, sys.stdin.readlines()))

# Assume we always start going right
def solve(n, costs):
    rights = ceil(n//2)
    ups = n//2
    smallest_right = 10**10
    smallest_up = 10**10
    rightsum = 0
    upsum = 0
    for i in range(0, n, 2):
        smallest_right = min(costs[i], smallest_right)
        rightsum += costs[i]
    for i in range(1, n, 2):
        smallest_up = min(costs[i], smallest_up)
        upsum += costs[i]
    rightsum -= smallest_right
    upsum -= smallest_up
    right_long = n - rights + 1
    up_long = n - ups + 1
    return rightsum + upsum + right_long*smallest_right + up_long*smallest_up

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    n = len(nums)
    print(solve(n, nums))



