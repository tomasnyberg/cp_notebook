import sys
import math
from heapq import heappush, heappop
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(counts, total):
    nums = [total]
    while nums:
        curr = heappop(nums)
        if curr == 1 and curr not in counts:
            print("NO")
            return
        if curr in counts:
            counts[curr] -= 1
            if counts[curr] == 0: del counts[curr]
        else:
            heappush(nums, curr//2)
            heappush(nums, math.ceil(curr/2))
    print("YES")

for i in range(1, len(lines),2 ):
    n = int(lines[i])
    nums = list(map(int, lines[i+1].split(" ")))
    total = 0
    counts = {}
    for x in nums:
        counts[x] = 1 if x not in counts else counts[x] + 1
        total += x
    solve(counts, total)