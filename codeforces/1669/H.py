import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    for i in range(30, -1, -1):
        needed_to_inc = len(nums)
        for num in nums:
            if num & (1 << i):
                # print(i, num, bin(num))
                needed_to_inc -= 1
        if needed_to_inc <= k:
            for idx, num in enumerate(nums):
                nums[idx] = num | (1 << i)
            k -= needed_to_inc
    result = 0b1111111111111111111111111111111
    for num in nums:
        result = result & num
    print(result)