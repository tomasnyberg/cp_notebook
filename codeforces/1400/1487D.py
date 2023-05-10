import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import bisect

# for i in range(1, 1000):
#     for j in range(i, 1000):
#         for k in range(1, 1000):
#             if i**2 + j**2 == k**2 and k == i**2 - j:
#                 print(i, j, k)
#                 break

curr = 4
increments = 8
good = [(3,4,5)]
i = 3
while curr < 10**9:
    i+= 2
    curr += increments
    increments += 4
    good.append((i, curr, curr+1))
assert all([x**2 + y**2 == z**2 and z == x**2 - y for x,y,z in good])
good = [g[2] for g in good]

for line in lines[1:]:
    n = int(line)
    print(bisect.bisect_right(good, n))

