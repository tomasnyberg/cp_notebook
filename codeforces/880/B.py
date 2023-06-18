import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))

# lines="""5
# 3 3 100
# 2 1 14
# 91 2 13
# 36 16 6
# 73 8 22""".split("\n")

for line in lines[1:]:
    n, k, g = map(int, line.split())
    # n to split between
    # k*g silver coins
    # We should distribute k gold coins among those n
    # 
    silver = k * g
    give = -1
    if g % 2 == 0:
        give = g // 2 - 1
    else:
        give = g // 2
    save = silver
    remaining = silver - give * n
    low = 0
    high = 10**10
    while low < high:
        mid = (low + high) // 2
        if remaining - mid * g > 0:
            low = mid + 1
        else:
            high = mid
    save -= low * g
    save = max(0, save)
    print(save)
        

