import sys
from heapq import heappop, heappush
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

# 6 3
# 0 9 8 7 6 5
# [0, 9, 8] = 1*(0-0) + 2*9 + 3 * (8-9) = 18 - 3 = 15 

for i in range(1, len(lines), 2):
    n, m = map(int, lines[i].split())
    nums = list(map(int, lines[i+1].split()))
    hq = []
    curr_tot_sum = 0
    result = -10**20
    for i, x in enumerate(nums):
        if len(hq) >= m-1:
            result = max(result, m * x - curr_tot_sum)
        curr_tot_sum += x
        heappush(hq, -x)
        if len(hq) == m:
            curr_tot_sum -= -heappop(hq)
    print(result)
