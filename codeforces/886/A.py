import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    nums = list(map(int, line.split()))
    nums.sort()
    print("YES" if nums[-1] + nums[-2] >= 10 else "NO")