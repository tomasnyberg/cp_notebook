import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

import math as mt
 
MAXN = 10**7 + 1
 
# stores smallest prime factor for
# every number
spf = [0 for i in range(MAXN)]
 
# Calculating SPF (Smallest Prime Factor)
# for every number till MAXN.
# Time Complexity : O(nloglogn)
def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
         
        # marking smallest prime factor
        # for every number to be itself.
        spf[i] = i
 
    # separately marking spf for
    # every even number as 2
    for i in range(4, MAXN, 2):
        spf[i] = 2
 
    for i in range(3, mt.ceil(mt.sqrt(MAXN))):
         
        # checking if i is prime
        if (spf[i] == i):
             
            # marking SPF for all numbers
            # divisible by i
            for j in range(i * i, MAXN, i):
                 
                # marking spf[j] if it is
                # not previously marked
                if (spf[j] == j):
                    spf[j] = i
sieve()
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

