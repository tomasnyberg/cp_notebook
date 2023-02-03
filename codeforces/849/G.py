import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split())
    line = lines[i+1]
    nums = list(map(int, line.split()))
    for i in range(len(nums)):
        nums[i] += i + 1
        nums[i] = (nums[i], i)
    nums.sort(key=lambda x: (-x[0], x[1]))
    result = 0 
    while nums and k >= nums[-1][0]:
        result += 1
        cost, idx = nums.pop()
        # print(cost, idx)
        k -= cost
    print(result)

    