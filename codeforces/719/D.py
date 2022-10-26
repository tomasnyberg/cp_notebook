import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    counts = {}
    res = 0
    for idx, x in enumerate(nums):
        curr = idx - x
        res += counts[curr] if curr in counts else 0
        counts[curr] = 1 if curr not in counts else counts[curr] + 1
    print(res)

        