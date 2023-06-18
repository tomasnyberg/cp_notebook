import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))

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
    result = 0
    for i in range(n + 1):
        one_and_a_half = i * (give + g)
        remaining = silver - one_and_a_half
        if i < n and math.ceil(remaining / (n - i)) >= give:
            continue
        else:
            result = max(result, silver - i*g)
    print(result)

        

