import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    to_reverse = []
    for i in range(len(nums)):
        if nums[i] != i+1:
            to_reverse.append(i)
    for i in range(len(to_reverse)//2):
        a, b = to_reverse[i], to_reverse[len(to_reverse) - i - 1]
        nums[a], nums[b] = nums[b], nums[a]
    print("YES" if nums == list(sorted(nums)) else "NO")

