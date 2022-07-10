from bisect import bisect
import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def min_amount(nums, target):
    if nums[-1] < target:
        return -1
    low = 0
    high = len(nums) 
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] == target:
            return mid + 1
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return max(low, high) + 1

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

i = 1
while i < len(lines):
    n, queries = map(int, lines[i].split(" "))
    i+=1
    nums = list(map(int, lines[i].split(" ")))
    nums.sort(key=lambda x: -x)
    CS = cum_sum(nums)
    i+=1
    while queries > 0:
        target = int(lines[i])
        # print(CS, target)
        print(min_amount(CS, target))
        queries -=1
        i+=1
    