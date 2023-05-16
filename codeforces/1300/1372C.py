import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    expected = [i for i in range(1, len(nums)+1)]
    if nums == expected:
        print(0)
        continue
    for _ in range(2):
        while nums and nums[-1] == expected[-1]:
            nums.pop()
            expected.pop()
        nums.reverse()
        expected.reverse()
    for i in range(len(nums)):
        if nums[i] == expected[i]:
            print(2)
            break
    else:
        print(1)