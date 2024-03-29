import sys
from heapq import heappop, heappush
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict


def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result


ii = 1
while ii < len(lines):
    n, m, k, d = map(int, lines[ii].split())
    ii += 1
    grid = []
    for _ in range(n):
        grid.append(list(map(lambda x: x+1, map(int, lines[ii].split()))))
        ii += 1

    def cost(i):
        hq = [(grid[i][0], 0)]
        result = [grid[i][0]]
        for j in range(1, len(grid[i])):
            while j - hq[0][1] > d + 1:
                heappop(hq)
            result.append(hq[0][0] + grid[i][j])
            heappush(hq, (result[-1], j))
        return result
    costs = []
    for i in range(len(grid)):
        costs.append(cost(i)[-1])
    cs = cum_sum(costs)
    result = 10**15
    for i in range(len(cs)):
        if i + k - 1 < len(cs):
            result = min(result, cs[i+k-1] - (cs[i-1] if i > 0 else 0))
    print(result)
