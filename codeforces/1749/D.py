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
for i in range(1, n+1):
    result += pow(m, i, MOD)
    result %= MOD
cur = 1
cnt = 1
for i in range(1,n+1):
    if i in primes:
        cur *= i
    cnt = cnt*(m//cur)
    result -= cnt
print(result % MOD)