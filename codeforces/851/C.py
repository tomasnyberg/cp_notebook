import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import itertools

# for i in range(3, 25,2):
#     a = [i for i in range(1, 2*i + 1)]
#     offset = (i-3)//2
#     b = [i-offset for i in range(i*2, i*2 + i)]
#     print(sum(a), a)
#     print(sum(b), b)
#     print()

# # All permutations of the first 10 natural numbers
# counts = [0]*12
# for perm in itertools.permutations(range(1, 11)):
#     prev = -1
#     good = True
#     for i in range(1, len(perm), 2):
#         if prev == -1:
#             prev = perm[i] + perm[i-1]
#         else:
#             if prev != perm[i] + perm[i-1] - 1:
#                 good = False
#                 break
#             prev = perm[i] + perm[i-1]
#     if good:
#         counts[perm[0]] += 1
#         print(perm)
# print(counts)

for line in lines[1:]:
    x = int(line)
    if x % 2 == 0:
        print("No")
        continue
    pairs = []
    offset = (x-3)//2
    target = 2*x - offset
    used = set()
    for i in range(1, 2*x + 1, 2):
        needed = target - i
        if needed <= i or needed in used or i in used:
            break
        pairs.append((i, needed))
        used.add(i)
        used.add(needed)
        target += 1
    for i in range(2, 2*x + 1, 2):
        needed = target - i
        if needed <= i or needed in used or i in used:
            break
        pairs.append((i, needed))
        target += 1
    print("Yes")
    for p in pairs:
        print(*p)
    