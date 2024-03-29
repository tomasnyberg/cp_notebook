import sys
lines = list(map(str.strip, sys.stdin.readlines()))

n = int(lines[0])
if n == 1 or n == 2:
    print(0)
    print(*list(map(int, lines[1].split(" "))))
    exit()

nums = list(map(int, lines[1].split(" ")))
nums.sort()
def check(x, nums, construct=False):
    if x == 0:
        if not construct:
            return len(nums) >= 1
        else:
            return nums
    nums = nums[:][::-1]
    to_insert = []
    result = []
    for _ in range(x):
        to_insert.append(nums.pop())
    to_insert.reverse()
    while to_insert:
        while nums and nums[-1] <= to_insert[-1]:
            result.append(nums.pop())
        if not nums:
            return False
        result.append(nums.pop())
        result.append(to_insert.pop())
    while nums:
        result.append(nums.pop())
    good = 0
    for i in range(1, len(result) - 1):
        if result[i-1] > result[i] < result[i+1]:
            good += 1
    # print(result, good, x)
    if not construct:
        return good >= x
    else:
        return result
check(3, nums)

low = 0
high = len(nums) - 1
while low < high:
    mid = (low + high) // 2
    if check(mid, nums):
        low = mid + 1
    else:
        high = mid
print(low-1)
print(*check(low-1, nums, True))
