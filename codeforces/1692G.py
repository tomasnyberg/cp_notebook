import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split(" "))
    k += 1
    nums = list(map(int, lines[i+1].split(" ")))
    nums = list(map(math.log2, nums))
    for i in range(len(nums)):
        nums[i] += i + 1
    bad_pairs = {}
    for i in range(len(nums) - 1):
        if nums[i+1] <= nums[i]:
            bad_pairs[i] = i+1
    curr_bad = set()
    for i in range(k-1):
        if i in bad_pairs:
            curr_bad.add(i)
    result = 0
    a = 0
    b = k-1
    while b < len(nums):
        # print(a, b, curr_bad)
        if not curr_bad:
            result += 1
        if a in curr_bad:
            curr_bad.remove(a)
        if b in bad_pairs:
            curr_bad.add(b)
        a+=1
        b+=1
    print(result)
    # print(nums)
    # print(bad_pairs)
    # print()