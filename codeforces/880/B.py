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
    def check(x): # Can we give x employees give money?
        given = x* give
        remaining = silver - given
        remaining_employees = n - x
        if remaining_employees*(give + g) >= remaining:
            return True
        else:
            return False
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            low = mid + 1
        else:
            high = mid
    if not check(low):
        low -= 1
    print(silver - ((n - (low))*g))
        

