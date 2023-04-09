import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check(xs):
    if len(xs) == 2:
        return xs[0] <= xs[1]
    count = 0
    for i in range(1, len(xs)):
        if (xs[i-1] if i-1 >= 0 else 10**15) > xs[i] < (xs[i+1] if i+1 < len(xs) else 10**15):
            count += 1
    return count <= 1

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    # print(nums)
    for i in range(1,len(nums)):
        if nums[i] >= 0:
            to_remove = nums[i]
            nums[i-1] -= to_remove
            nums[i] = 0
    total_add = 0
    # print(nums)
    for i in range(1, len(nums) - 1):
        if nums[i] < nums[i-1]:
            to_add = nums[i-1] - nums[i]
            nums[i] += to_add
            nums[i + 1] += to_add
    # print(nums)
    a = nums == list(sorted(nums))
    print("YES" if a else "NO")
    