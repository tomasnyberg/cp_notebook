import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 4):
    n = int(lines[i])
    m = int(lines[i+2])
    nums = list(map(int, lines[i+1].split()))
    shuffles = list(map(int, lines[i+3].split()))
    print(nums[sum(shuffles) % n])