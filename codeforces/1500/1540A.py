import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    nums.sort()
    result = nums[-1]
    cs = cum_sum(nums)
    # A number is going to contribute with the sum of all numbers after it,
    # minus the amount of numbers after it - itself
    for idx, x in enumerate(nums):
        result -= cs[-1] - cs[idx] - (len(nums) - idx - 1)*x
    print(result)