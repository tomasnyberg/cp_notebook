from collections import deque
import sys
lines = list(map(str.strip, sys.stdin.readlines()))


def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

def check_swap_immediately(nums, k, first):
    total = sum(nums[1:]) + first
    if total <= k:
        return nums[0] - first
    count = 0
    for i in range(len(nums) - 1,0,-1):
        count += 1
        total -= nums[i] - first
        if total <= k:
            return count + (nums[0] - first)
    return -1


for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    total = sum(nums)
    nums.sort()
    test = check_swap_immediately(nums, k, nums[0])
    if test != -1:
        print(test)
        continue
    low = 0
    high = 10**35
    result = 10**35
    while low < high:
        mid = (low + high) // 2
        test = check_swap_immediately(nums, k, nums[0] - mid)
        if test != -1:
            high = mid
        else:
            low = mid + 1
    for i in range(low, low + 15):
        result = min(result, check_swap_immediately(nums, k, nums[0] - i))
    print(result)



