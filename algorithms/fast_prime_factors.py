# A fast way to get prime factors of a number if you need to do it a bunch of times.

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

def prime_factors_slow(x):
    res = []
    for i in range(2, math.ceil(math.sqrt(x))):
        while x % i == 0:
            res.append(i)
            x //= i
    if x != 1:
        res.append(x)
    return res
