import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from bisect import bisect_left
from functools import lru_cache
from collections import Counter

import math
N = 2*10**5 + 100
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
    ret = {}
    while (x != 1):
        ret[spf[x]] = ret.get(spf[x], 0) + 1
        x //= spf[x]
    return ret


from itertools import product

# Quickly generates divisors, time complexity approximately O(d) where d is the number of divisors.
# For n < 200 000 the biggest d is approx 160, so O(nd) usually fits within constraints.
def generate_divisors(prime_factors):
    # For each prime factor, generate a list of its powers up to its exponent.
    factor_powers = [ [prime**exp for exp in range(factor_exp + 1)] for prime, factor_exp in prime_factors.items()]
    
    # Generate all combinations of these powers using Cartesian product.
    divisors = {1}
    for combination in product(*factor_powers):
        divisor = 1
        for val in combination:
            divisor *= val
        divisors.add(divisor)
    
    return sorted(divisors)
