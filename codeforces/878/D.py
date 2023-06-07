import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import bisect
 

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    nums.sort()
    low = 0
    high = 10**9
    while low < high:
        mid = (low + high) // 2
        first = nums[0] + mid
        idx = bisect.bisect_right(nums, first + mid)
        if idx == len(nums):
            high = mid
            continue
        second = nums[idx] + mid
        idx2 = bisect.bisect_right(nums, second + mid)
        if idx2 == len(nums):
            high = mid
            continue
        third = nums[idx2] + mid
        if abs(nums[-1] - third) <= mid:
            high = mid
        else:
            low = mid + 1
    print(low)
    
