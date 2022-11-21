import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    withidx = list(enumerate(nums))
    withidx.sort(key=lambda x: x[1])
    for idx, x in enumerate(nums):
        if idx == withidx[-1][0]:
            print(x - withidx[-2][1], end=" ")
        else:
            print(x - withidx[-1][1], end=" ")
    print()