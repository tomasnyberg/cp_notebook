import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))
def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for i in range(1, len(lines),2 ):
    n, x = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    nums.sort()
    CS = cum_sum(nums)
    result = 0
    # print(nums)
    for j in range(len(nums)):
        days_we_can = math.ceil((x-CS[j])/(j+1))
        if CS[j] + (days_we_can + 1)*(j) <= x:
            days_we_can += 1
        # print("we can buy", j, "for", days_we_can, "days")
        result += days_we_can if days_we_can > 0 else 0
    print(result)