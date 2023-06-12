import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import defaultdict
from functools import lru_cache
import bisect

ii = 1
while ii < len(lines):
    n = int(lines[ii])
    ii+=1
    ranges = []
    for _ in range(n):
        l, r = list(map(int, lines[ii].split()))
        ranges.append((l, r))
        ii+=1
    ranges.sort()
    @lru_cache(None)
    def recur(i):
        if i == len(ranges):
            return 0
        result = 10**9
        removed = 0
        for j in range(i+1, len(ranges)):
            if ranges[j][0] > ranges[i][1]:
                break
            extra = 0
            k = j + 1
            while k < len(ranges) and ranges[k][0] <= max(ranges[j][1], ranges[i][1]):
                extra += 1
                k += 1
            result = min(result, removed + extra + recur(k))
            removed += 1
        return min(result, 1 + recur(i+1))
    print(recur(0))

        