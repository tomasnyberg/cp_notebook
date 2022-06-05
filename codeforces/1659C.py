import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for i in range(1, len(lines), 2):
    n, a, b = map(int, lines[i].split(" "))
    nums = [0] + list(map(int, lines[i+1].split(" ")))
    cumulative = cum_sum(nums)
    smallest = float("inf")
    for f in range(0, n+1):
        curr = a*nums[f]+b*(cumulative[-1] - cumulative[f] - (n-f-1)*nums[f])
        smallest = min(curr, smallest)
    print(smallest)

