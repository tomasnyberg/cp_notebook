import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache
from bisect import bisect_right

sys.setrecursionlimit(100000)


for line in lines[2::2]:
    nums = list(map(int, line.split()))
    # How many balls can we remove from index i onward
    indices = {}
    for i, x in enumerate(nums):
        if x not in indices:
            indices[x] = []
        indices[x].append(i)
    maxes = [False]*(len(nums) + 1)
    @lru_cache(None)
    def recur(i):
        if i == len(nums):
            return 0
        idx = bisect_right(indices[nums[i]], i)
        new_idx = -1 if idx == len(indices[nums[i]]) or indices[nums[i]][idx] <= i else indices[nums[i]][idx]
        if new_idx == -1:
            return recur(i+1)
        b = recur(new_idx) + new_idx - i + 1
        if b > recur(i+1):
            maxes[i] = True
        if maxes[new_idx]:
            b-=1
        return max(recur(i+1), b)
    print(recur(0))
        

