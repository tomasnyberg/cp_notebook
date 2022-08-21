import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def cost_to_make_equal(xs):
    result = 0
    for i in range(1, len(xs)):
        result += abs(xs[i]-xs[i-1])
    return result

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    possibilities = set(nums)
    best = cost_to_make_equal(nums) # No changes
    max_dec = max(abs(nums[0] - nums[1]), abs(nums[-1]- nums[-2]))
    for i in range(1, len(nums)- 1):
        max_dec = max(max_dec, abs(nums[i]-nums[i-1]) + abs(nums[i+1] - nums[i]) - abs(nums[i+1]-nums[i-1]))
    print(best - max_dec)