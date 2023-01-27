import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    nums.sort()
    # print(nums)
    wants = {}
    for num in nums:
        # print(wants)
        if num-1 in wants:
            wants[num] = wants.get(num, 0) + 1
            wants[num-1]-=1
            if wants[num-1] == 0:
                del wants[num-1]
        else:
            wants[num] = wants.get(num, 0) + 1
    print(sum(wants.values()))