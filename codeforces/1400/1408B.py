from enum import unique
import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    uniquenums = len(set(nums))
    if k == 1:
        print(-1 if uniquenums != 1 else 1)
        continue
    if k >= uniquenums:
        print(1)
        continue
    print(math.ceil((uniquenums - k) / (k-1)) + 1)
