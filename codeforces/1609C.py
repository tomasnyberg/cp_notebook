import sys
lines = list(map(str.strip, sys.stdin.readlines()))
 
def sieve(num):
    prime = [True for _ in range(num+1)]
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
 
primes = set(sieve(10**6 + 1))
for i in range(1, len(lines),2 ):
    n, e = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    result = 0
    visited = set()
    for idx, num in enumerate(nums):
        if idx in visited: continue
        if num in primes or num == 1:
            found_prime = num in primes
            ones_before = 1 if num == 1 else 0
            ones_after = 0
            start = idx
            while idx + e < len(nums) and (nums[idx+e] in primes or nums[idx+e] == 1):
                if found_prime and nums[idx+e] in primes:
                    break 
                if not found_prime and (nums[idx+e] == 1 or nums[idx+e] in primes):
                    visited.add(idx+e)
                if nums[idx+e] in primes:
                    found_prime = True
                if not found_prime and nums[idx+e] == 1:
                    ones_before += 1
                elif found_prime and nums[idx+e] == 1:
                    ones_after += 1
                idx += e
            if found_prime:
                result += ones_before*(ones_after+1) + ones_after
    print(result)