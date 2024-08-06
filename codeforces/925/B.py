import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    expected = sum(nums) // len(nums)
    extra = 0
    for num in nums:
        if num < expected:
            if expected - num > extra:
                print("NO")
                break
            extra -= expected - num
        else:
            extra += num - expected
    else:
        if extra == 0:
            print("YES")
        else:
            print("NO")
