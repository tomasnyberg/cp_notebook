import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    total = sum(nums)
    print("YES" if int(math.sqrt(total)) == math.sqrt(total) else "NO")