import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def nCr(n,r):
    import math
    return math.factorial(n) // (math.factorial(r)*(math.factorial(n-r)))

for n in lines[1::2]:
    print(6*nCr(10 - int(n), 2))
