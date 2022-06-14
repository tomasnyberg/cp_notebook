import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split(" "))
    k += 1
    nums = list(map(int, lines[i+1].split(" ")))
    nums = list(map(math.log2, nums))
    left = 0
    right = k
    result = 0
    while right <= len(nums):
        sub = nums[left:right]
        holds = True
        for i in range(1, len(sub)):
            sub[i] += i
            if sub[i] <= sub[i-1]:
                holds = False
                break
        if holds:
            # print(sub)
            result += 1
        # print(sub)
        left += 1
        right += 1
    print(result)