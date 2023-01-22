import sys
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    candidate = [nums[0]]
    for x in nums[1:]:
        if x != 0 and candidate[-1] - x >= 0:
            print(-1)
            break
        candidate.append(x + candidate[-1])
    else:
        print(*candidate)