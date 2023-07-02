import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))

# def sieve(num):
#     prime = [True for i in range(num+1)]
#     result = set()
#     p = 2
#     while (p * p <= num):
#         if (prime[p] == True):
#             for i in range(p * p, num+1, p):
#                 prime[i] = False
#         p += 1
#     for p in range(2, num+1):
#         if prime[p]:
#             result.add(p)
#     return result
# primes = sieve(10**5)
# print(len(primes))

# def count_primes(xs):
#     return sum(1 for x in xs if x in primes)

# def brute_force(n):
#     items = [i for i in range(1, n)]
#     longest = []
#     for mask in range(1 << (n-1)):
#         prod = 1
#         taken = []
#         for i, x in enumerate(items):
#             if mask & (1 << i):
#                 prod *= x
#                 taken.append(x)
#         if prod % n == 1:
#             if len(taken) > len(longest):
#                 longest = taken
#             if len(taken) == len(longest):
#                 if count_primes(taken) > count_primes(longest):
#                     longest = taken
    # return longest
# # All numbers which have no common prime factors?
# def prime_factors(x):
#     ret = list()
#     while (x != 1):
#         ret.append(spf[x])
#         x //= spf[x]
#     return ret

# for i in range(2, 33):
#     print(i,prime_factors_slow(i), brute_force(i))

import math
N = 10**6 + 1
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

def prime_factors(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x //= spf[x]
    return ret

for line in lines:
    n = int(line)
    pfs = set(prime_factors(n))
    result = []
    for i in range(1, n):
        curr_pfs = set(prime_factors(i))
        if len(curr_pfs.intersection(pfs)) == 0:
            result.append(i)
    prod = 1
    for x in result:
        prod *= x
        prod %= n
    if prod % n != 1:
        prod //= result.pop()
    # assert prod % n == 1
    print(len(result))
    print(*result)
    # print("mod", prod % n, prod, n)
