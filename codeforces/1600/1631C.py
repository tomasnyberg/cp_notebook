import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque
# import random

# def find_sum(n):
#     def total_and(nums):
#         q = deque(nums)
#         total = 0
#         while q:
#             a, b = q.pop(), q.pop()
#             total += a & b
#         return total
#     # n = 2**n
#     nums = [i for i in range(n)]
#     return total_and(nums)

# maxes = {}
# for i in range(2,17):
#     maxes[2**i] = find_sum(2**i)

# print(maxes)

# print(find_sum(2**16))

# def solve(n, k):
#     nums = i for i in range


for line in lines[1:]:
    n, k = map(int, line.split(" "))
    mappings = {}
    for i in range(n // 2):
        mappings[i] = n - i - 1
    if k == n-1:
        if n == 4:
            print(-1)
            continue
        mappings[n-1] = n-2
        mappings[1] = 3
        mappings[0] = n-4
        del mappings[3]
    else:
        mappings[k] = n-1
        mappings[n-k-1] = 0
        del mappings[0]

    for x in mappings:
        if mappings[x] not in mappings:
            print(x, mappings[x])

        k-=x & mappings[x]
    assert k == 0

