import sys
lines = list(map(str.strip, sys.stdin.readlines()))

import random

def split_number(x):
    if x % 3 != 0: return (0, 0)
    double = 2 * x
    half = double // 3
    return (half, x - half)

# for _ in range(10):
#     x = random.randint(1, 1000)
#     print(x, split_number(x))


for line in lines[1:]:
    n, m = map(int, line.split(" "))
    if n == m:
        print("YES")
        continue
    if n < m:
        print("NO")
        continue
    nums = [n]
    found = False
    while nums:
        nxt = nums.pop()
        a, b = split_number(nxt)
        if a == 0 and b == 0: continue
        if a == m or b == m:
            found = True
            break
        nums.append(a)
        nums.append(b)
    print("YES" if found else "NO")