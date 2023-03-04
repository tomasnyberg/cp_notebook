import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def nCr(n,r):
    import math
    return math.factorial(n) // (math.factorial(r)*(math.factorial(n-r)))

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

primes = sieve(10**6 + 5)
nums = list(map(int, lines[1].split(" ")))
primes_only= []
exponents = []
already_seen_primes = set()
for num in nums:
    if num in primes and num not in already_seen_primes:
        primes_only.append(num)
        already_seen_primes.add(num)
    else:
        exponents.append(num)
if len(primes) < len(exponents):
    print(0)
    exit()

seen = set()
def recur(primes, nonprimes, product, taken):
    print("Recur with", primes, nonprimes, product, taken)
    if not primes and not nonprimes:
        seen.add(product)
        return
    thistaken = set(taken)
    # Then we can match a prime with a prime
    if len(primes) - len(nonprimes) >= 2:
        for i in range(len(primes)):
            if primes[i] in thistaken: continue
            for j in range(i+1, len(primes)):
                print("taking", primes[i], primes[j])
                thistaken.add(primes[i])
                recur(primes[:i] + primes[i+1:j] + primes[j+1:], nonprimes, product * primes[i]**primes[j], thistaken)
                thistaken.remove(primes[i])
    for i in range(len(primes)):
        if primes[i] in thistaken: continue
        for j in range(len(nonprimes)):
            print("taking", primes[i], nonprimes[j])
            thistaken.add(primes[i])
            recur(primes[:i] + primes[i+1:], nonprimes[:j] + nonprimes[j+1:], product * primes[i]**nonprimes[j], thistaken)
recur(primes_only, exponents, 1, set())
print(seen)
        