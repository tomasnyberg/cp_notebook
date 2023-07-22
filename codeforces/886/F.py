import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from bisect import bisect_left
from functools import lru_cache
from collections import Counter

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    n = len(nums)
    nums = [x for x in nums if x <= len(nums)]
    counts = dict(Counter(nums))
    scores = [0 for _ in range(n + 1)]
    for k, v in counts.items():
        i = 0
        while i < n + 1:
            scores[i] += v
            i += k
    scores.pop(0)
    print(max(scores))

