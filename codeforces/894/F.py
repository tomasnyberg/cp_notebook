import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 3):
    w, f= map(int, lines[ii].split())
    n = int(lines[ii+1]) 
    nums = list(map(int, lines[ii + 2].split()))
    def check(mid):
        water, fire = mid*w, mid*f
        @lru_cache(None)
        def recur(i, waterloo, fireloo): # 100*100*10^4
            if i == len(nums):
                return True
            result = False
            if waterloo >= nums[i]:
                result |= recur(i + 1, waterloo - nums[i], fireloo)
            if fireloo >= nums[i]:
                result |= recur(i + 1, waterloo, fireloo - nums[i])
            return result
        return recur(0, water, fire)
    low = 0
    high = 10**9
    while low <= high:
        mid = (low + high) >> 1
        if check(mid):
            high = mid - 1
        else:
            low = mid + 1
    print(mid if check(mid) else mid +1)
