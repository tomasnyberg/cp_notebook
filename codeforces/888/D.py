import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import Counter
# TODO Remember to add int wrapping if using dict

from random import getrandbits

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

def prefix_sum_to_array(prefix_sum):
    if not prefix_sum:
        return []
    original_array = [prefix_sum[0]]
    for i in range(1, len(prefix_sum)):
        original_array.append(prefix_sum[i] - prefix_sum[i-1])
    return original_array

def is_permutation_of_length(n, xs):
    return sorted(xs) == list(range(1, n+1))

def perm_sum(n):
    return n * (n+1) // 2

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    n = len(nums) + 1
    expected_sum = perm_sum(len(nums) + 1)
    if nums[-1] > expected_sum:
        print("NO")
        continue
    if nums[-1] < expected_sum:
        nums.append(expected_sum)
        arr = prefix_sum_to_array(nums)
        print("YES" if is_permutation_of_length(len(nums), arr) else "NO")
        continue
    permset = set([Wrapper(i) for i in list(range(1, n+1))])
    arr = prefix_sum_to_array(nums)
    missing = list(permset - set([Wrapper(i) for i in arr]))
    notexpected = []
    seen = set()
    for x in arr:
        if Wrapper(x) in seen or Wrapper(x) not in permset:
            notexpected.append(x)
        seen.add(Wrapper(x))
    print("YES" if len(missing) == 2 and len(notexpected) == 1 and missing[0] + missing[1] == notexpected[0] else "NO")
    # permset = set(list(range(1, n+1)))
    # arr = prefix_sum_to_array(nums)
    # missing = list(permset - set(arr))
    # notexpected = []
    # seen = set()
    # for x in arr:
    #     if x in seen or x not in permset:
    #         notexpected.append(x)
    #     seen.add(x)
    # # print("original", nums)
    # # print("array", arr)
    # # print("missing", missing)
    # # print("unexpected", notexpected)
    # print("YES" if len(missing) == 2 and len(notexpected) == 1 and missing[0] + missing[1] == notexpected[0] else "NO")

