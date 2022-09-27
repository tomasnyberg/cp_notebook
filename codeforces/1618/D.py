import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, k= map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    nums.sort()
    result = 0
    taken = set()
    while k > 0:
        i = len(nums)-1
        while i in taken:
            i-=1
        taken.add(i)
        target = i - k
        while target in taken:
            target -= 1
        result += nums[target] // nums[i]
        assert(target not in taken)
        # print(i, target)
        taken.add(target)
        k-=1
    for idx, x in enumerate(nums):
        if idx not in taken:
            result += x
    print(result)
    # print()
