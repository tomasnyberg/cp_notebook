import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    candidates = [[nums[i] if i % 2 == j else 1 for i in range(len(nums))] for j in range(2)]
    for candidate in candidates:
        if 2*sum([abs(nums[i] - candidate[i]) for i in range(len(candidate))]) <= sum(nums):
            [print(x, end =" ") for x in candidate]
            break
    print()