import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import random

def is_good_array(arr):
    n = len(arr)
    for l in range(n):
        for r in range(l, n):
            subsegment_sum = sum(arr[l:r+1])
            expected_sum = (arr[l] + arr[r]) * (r - l + 1) / 2
            if subsegment_sum != expected_sum:
                return False
    return True

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    longest = 1
    for i in range(len(nums)):
        for other in range(i+1, len(nums)):
            for steps in range(1, 100):
                if i + steps > other: break
                if (other - i) % steps: continue
                diff = (nums[other] - nums[i]) / ((other-  i) //steps)
                count = 1
                mul = 1
                for j in range(i + steps, len(nums), steps):
                    if nums[j] == (nums[i] + diff * mul):
                        count += 1
                    mul += 1
                # print(i, other, steps, diff, count)
                longest = max(longest, count)
    print(len(nums) - longest)
                
    