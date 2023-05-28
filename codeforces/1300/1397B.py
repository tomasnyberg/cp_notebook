import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1::2]:
    nums = list(map(int, line.split()))
    nums.sort()
    result = sum(x - 1 for x in nums)
    for i in range(2, 100000):
        pwr = i**(len(nums) - 1)
        if pwr > nums[-1] and pwr - nums[-1] > result:
            break
        result = min(result, sum(abs(x - i**j) for j, x in enumerate(nums)))
    print(result)
    # print(sum(nums))
    