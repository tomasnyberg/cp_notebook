import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque
import random

def find_sum(n):
    def total_and(nums):
        q = deque(nums)
        total = 0
        while q:
            a, b = q.pop(), q.pop()
            total += a & b
        return total
    # n = 2**n
    nums = [i for i in range(n)]
    return total_and(nums)

maxes = {}
for i in range(2,17):
    maxes[2**i] = find_sum(2**i)

print(maxes)

def solve(n, k):
    nums = [i for i in range(n)]
    q = deque(nums)
    pairs = []
    while k - q[-1] & q[-2] >= 0:
        a, b = q.pop(), q.pop()
        k-= a & b
    assert k == 0 or k < q[-1] + 1
    # if k > 0:
    #     print(k, bin(k), q[-1], bin(q[-1]), len(bin(q[-1])[2:]), len(bin(k)[2:]))
    # print(k,q)
    # for x in q:
    #     print(bin(x)[2:].zfill(max([len(bin(x)[2:]) for x in q])))

for i in range(1000000):
    solve(2**8, random.randint(0, maxes[2**8]))


for line in lines[1:]:
    n, k = map(int, line.split(" "))
    if k > maxes[n]:
        print(-1)
        continue

