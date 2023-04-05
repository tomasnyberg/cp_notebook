import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

for line in lines[1:]:
    a, b = map(int, line.split())
    g = gcd(a, b)
    # print(g)
    result = g - 1
    result += a // g
    best = 10**25
    factors = [1] + prime_factors(b)
    # print(factors, result)
    prod = 1
    for factor in factors:
        prod *= factor
        # if prod < g: continue
        best = min(best, result + max(prod - g, 0) + (b//prod))
    print(best)

    # print(g-1 + (a)//g + (b)//g)