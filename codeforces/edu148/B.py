import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    nums.sort()
    CS = cum_sum(nums)
    result = 0
    # print(nums)
    # print(CS)
    for i in range(0,n,2):
        remainingops = k - (i//2)
        # print(i, remainingops, CS[-1-remainingops])
        result = max(result, CS[-1-remainingops] - (CS[i-1] if i > 0 else 0))
    print(result)

    



