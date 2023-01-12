import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

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

