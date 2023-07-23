# If you are using dictionaries with integers as keys, there is a possibility
# that someone hacks your solution by submitting a test case with keys that
# cause hash collisions, which will make your solution run in O(n^2) time.
# Wrapping them in ints like this 

from random import getrandbits

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

# EXAMPLE: https://codeforces.com/contest/1850/problem/F
# If you do not wrap the int x here, it will TLE on test case 42.

# for line in lines[2::2]:
#     nums = list(map(int, line.split()))
#     n = len(nums)
#     nums = [Wrapper(x) for x in nums if x <= len(nums)]
#     counts = dict(Counter(nums))
#     scores = [0 for _ in range(n + 1)]
#     for k, v in counts.items():
#         i = 0
#         while i < n + 1:
#             scores[i] += v
#             i += k
#     scores.pop(0)
#     print(max(scores))


