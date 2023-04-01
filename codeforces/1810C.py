import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, c, d = map(int, lines[i].split())
    nums = list(map(int, lines[i + 1].split()))
    result = 0
    seen = set()
    for num in nums:
        if num in seen:
            result += c
        seen.add(num)
    nums = list(sorted(set(nums)))
    other = 10**25
    for idx, x in enumerate(nums):
        missing = (x - idx - 1)*d
        to_delete = (len(nums) - idx - 1)*c
        other = min(other, (missing + to_delete))
    print(min(result + other, n*c+d))
