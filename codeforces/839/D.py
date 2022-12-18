import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

def bs(a, b):
    big = max(a,b )
    small = min(a,b)
    low = min(a, b)
    high = max(a, b)
    while low < high:
        mid = (low + high) // 2
        print(mid)
        if big - mid < abs(small - mid):
            low = mid + 1
        else:
            high = mid
    return low


for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if nums == sorted(nums):
        print(0)
    elif nums == sorted(nums, reverse=True):
        print(nums[0])
    elif nums[0] == nums[-1] and nums[0] % 2 == nums[1] % 2 and all(nums[i] == nums[i+1] for i in range(1, len(nums)-2)):
        print(math.ceil((nums[-1] + nums[-2]) / 2))
    elif nums[:-1] == sorted(nums[:-1]): # TODO, the last number is smaller than the rest, or the first number is bigger than the rest
        candidate = math.ceil((nums[-2] + nums[-1]) / 2)
        for i in range(len(nums)):
            nums[i] = abs(nums[i] - candidate)
        if nums == sorted(nums):
            print(candidate)
        else:
            print(-1)
    else:
        print(-1)