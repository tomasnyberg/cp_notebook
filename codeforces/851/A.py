import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check(k, nums):
    prod1 = nums[0]
    for i in range(1, k):
        prod1 *= nums[i]
    prod2 = 1
    for i in range(k, len(nums)):
        prod2 *= nums[i]
    # print(k, prod1, prod2)
    return prod1 == prod2

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    for k in range(1, len(nums)):
        if check(k, nums):
            print(k)
            break
    else:
        print(-1)

