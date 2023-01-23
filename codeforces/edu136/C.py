import sys
import itertools
import math
lines = list(map(str.strip, sys.stdin.readlines()))

MOD = 998244353

def nCr(n,r):
    import math
    return math.factorial(n) // (math.factorial(r)*(math.factorial(n-r)))

def calc(n):
    if n == 2:
        return [1, 0, 1]
    a = calc(n-2)
    return [nCr(n-1, n//2) + a[1], nCr(n-2, n//2) + a[0], 1] 

for line in lines[1:]:
    n = int(line)
    print(*list(map(lambda x: x % MOD, calc(n))))

