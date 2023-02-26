import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

def solve(target, nums):
    needed = 0
    for x in nums:
        needed += target - x
    low = 0
    high = 10**20
    res = -1
    while low <= high:
        mid = (low + high) // 2
        cnt1 = (mid + 1)//2; cnt2 = mid // 2
        need1 = 0
        for x in nums:
            cur = (target -x) //2
            if(target - x) % 2 == 1:
                need1 += 1
            if cnt2 >= cur:
                cnt2 -= cur
            else:
                cur -= cnt2
                cnt2 = 0
                need1 += cur*2
        if need1 <= cnt1:
            res = mid
            high = mid - 1
        else:
            low = mid + 1 
    return res

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    biggest = max(nums)
    targets = [biggest, biggest + 1]
    result = 10**20
    for target in targets:
        result = min(solve(target, nums), result)
    print(result)