import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

import math
N = 10**7 + 1
# stores smallest prime factor for every number
spf = [0 for i in range(N)]
def sieve():
    spf[1] = 1
    for i in range(2, N):
        spf[i] = i
    for i in range(4, N, 2):
        spf[i] = 2
    for i in range(3, math.ceil(math.sqrt(N))):
        # Is i prime=
        if (spf[i] == i):
            # in that case, mark the spf of all numbers divisible by i as i
            # (But only mark them if they have not previously been marked by a smaller number)
            for j in range(i * i, N, i):
                spf[j] = i if spf[j] == j else spf[j]
sieve()

# Very quickly finds the prime factors, since we always know what the
# next one is.
def prime_factors(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x //= spf[x]
    return ret


for line in lines[1:]:
    a, b = map(int, line.split())
    if abs(a - b) == 1:
        print(-1)
        continue
    if gcd(a, b) != 1:
        print(0)
        continue
    a, b = min(a, b), max(a, b)
    ps = prime_factors(b-a)
    ans = 10**9
    for p in ps:
        ans = min(ans, p-(a%p))
    print(ans)

