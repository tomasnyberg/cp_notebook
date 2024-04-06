import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict
from collections import Counter
from itertools import permutations

def test(xs):
    mod = xs[0]
    for x in xs[1:]:
        mod = mod % x
    return mod != 0

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if nums.count(1) >= 2:
        print("NO")
        continue
    counts = dict(Counter(nums))
    smallest = min(nums)
    if counts[smallest] == 1:
        print("YES")
        continue
    for x in set(nums):
        if x % smallest != 0:
            print("YES")
            break
    else:
        print("NO")
    