import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    smallest = 10**9
    if len(line) <= 2:
        print(int(line))
        continue
    # print("-------------")
    # print(line)
    for skip in range(1, len(line)):
        nums = []
        for i in range(len(line)):
            if i == skip:
                continue
            if i+1 == skip:
                curr = int(line[i] + line[i+1])
            else:
                curr = int(line[i])
            nums.append(curr)
        # print(line, nums)
        if all(x == 1 for x in nums):
            smallest = min(smallest, 1)
            continue
        if 0 in nums:
            smallest = 0
            break
        result = 0
        # print(nums)
        for i in range(len(nums)):
            if nums[i] == 1:
                continue
            else:
                result += nums[i]
        smallest = min(smallest, result)
    print(smallest)
