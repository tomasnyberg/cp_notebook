import sys
from math import ceil
lines = list(map(str.strip, sys.stdin.readlines()))

# Assume we always start going right
def solve(n, costs):
    oddcnt = 0
    evencnt = 0
    oddsum = 0
    evensum = 0
    small_even = 10**20
    small_odd = 10**20
    result = 10**30
    for i in range(n):
        if i % 2 == 0:
            small_even = min(small_even, costs[i])
        else:
            small_odd = min(small_odd, costs[i])
        result = min(result, oddsum + (n-oddcnt)*small_odd + evensum + (n-evencnt)*small_even)
        if i % 2 == 0:
            evencnt += 1
            evensum += costs[i]
        else:
            oddcnt += 1
            oddsum += costs[i]
    return result
    
for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    n = len(nums)
    print(solve(n, nums))
