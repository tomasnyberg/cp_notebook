import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    remaining = set([i+1 for i in range(len(nums))])
    while len(remaining) > 1:
        a = -1
        b = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] -= 1
                if a == -1:
                    a = i
                else:
                    b = i
                    break
        if nums[a] == 0:
            remaining.remove(a+1)
        if nums[b] == 0:
            remaining.remove(b+1)
    print(remaining.pop())
