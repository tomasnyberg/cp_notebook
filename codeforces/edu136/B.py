import sys
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    ends = set()
    @lru_cache(None)
    def dfs(i, taken):
        if len(ends) > 1:
            return
        if i == len(nums):
            ends.add(taken)
            return 
        a = nums[i] + taken[-1]
        b = taken[-1] - nums[i]
        if a >= 0:
            dfs(i+1, taken + (a,))
        if b >= 0:
            dfs(i+1, taken + (b,))
        return 
    dfs(1, (nums[0],))
    # print(ends)
    print(*ends.pop() if len(ends) == 1 else [-1])