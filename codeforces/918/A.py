import sys
from collections import Counter
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    nums = list(map(int, line.split()))
    counts = Counter(nums)
    for k, v in counts.items():
        if v == 1:
            print(k)
            break
