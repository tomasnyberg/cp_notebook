import sys
lines = list(map(str.strip, sys.stdin.readlines()))

n, m = map(int, lines[0].split())
MOD = 998244353
def sieve(num):
    prime = [True for i in range(num+1)]
    result = set()
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            result.add(p)
    return result
primes = sieve(n + 1)
result = 0
divisor = 1
count = 1
for i in range(1, n+1):
    if i in primes:
        divisor *= i
    result += pow(m, i, MOD)
    count *= m // divisor
    result -= count
    result %= MOD
print(result % MOD)