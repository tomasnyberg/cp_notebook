import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import Counter
from random import getrandbits

# TODO Remember to add int wrapping if using dict

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    a = [nums[i] if i%2 == 1 else 0 for i in range(len(nums))]
    b = [nums[i] if i%2 == 0 else 0 for i in range(len(nums))]
    xs = []
    running = 0
    for i in range(len(a)):
        running += a[i]
        running -= b[i]
        xs.append(running)
    if 0 in xs:
        print("YES")
        continue
    xs = [Wrapper(x) for x in xs]
    counts = {}
    counts = dict(Counter(xs))
    for k, v in counts.items():
        if v >= 2:
            print("YES")
            break
    else:
        print("NO")
