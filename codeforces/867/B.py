import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    # print(nums)
    nums.sort()
    a = nums[0] * nums[1]
    b = nums[-1] * nums[-2]
    smallestneg = -10**12
    smallestpos = 10**12
    for x in nums:
        if x >= 0:
            smallestpos = min(x, smallestpos)
        else:
            smallestneg = max(x, smallestneg)
    c = smallestneg * smallestpos if smallestneg != -10**12 and smallestpos != 10**12 else -10**12
    print(max(a, b, c))