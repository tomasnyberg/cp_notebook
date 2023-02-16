import sys
lines = list(map(str.strip, sys.stdin.readlines()))
def nCr(n,r):
    import math
    return math.factorial(n) // (math.factorial(r)*(math.factorial(n-r)))
n = int(lines[0])
weights = list(map(int, lines[1].split()))
prod = 1
for i in range(0, len(weights), 3):
    a = weights[i]
    b = weights[i+1]
    c = weights[i+2]
    one = a + b
    two = a + c
    three = b + c
    m = max(one, two, three)
    maxcount = 0
    for x in [one, two, three]:
        if x == m:
            maxcount += 1
    prod *= maxcount
print((nCr((n//3), (n//6)) * prod) % 998244353)
    