import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from itertools import permutations

def construct_b(perm):
    result = []
    for i in range(len(perm)):
        total = 0
        for j in range(i+1):
            total += perm[j]
        result.append(total % len(perm) + 1)
    return result

def super_perm_check(perm):
    b = construct_b(perm)
    return list(sorted(b)) == list(sorted(perm))

for line in lines[1:]:
    x = int(line)
    if x == 1:
        print(1)
        continue
    if x % 2 == 1:
        print(-1) 
        continue
    xs = []
    for i in range(x):
        if i % 2 == 0:
            xs.append(x - i)
        else:
            xs.append(i)
    print(*xs)
        


