import sys
lines = list(map(str.strip, sys.stdin.readlines()))

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

primes = set(sieve(10**6 + 1))
for i in range(1, len(lines),2 ):
    n, e = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    prim = []
    result = 0
    visited = set()
    for idx, num in enumerate(nums):
        if idx in visited: continue
        if num in primes:
            ptr = idx
            ones_in_path = 0
            visited = set()
            while ptr+e < len(nums) and (nums[ptr+e] == 1 or nums[ptr+e] in primes):
                # print(idx+1, ones_in_path + 1)
                if nums[ptr+e] in primes:
                    result += (ones_in_path*(ones_in_path+1)) // 2
                    if ptr+e in visited:
                        visited.remove(ptr+e)
                    break
                ones_in_path +=1
                ptr += e 
                visited.add(ptr)
            result += ones_in_path
        if num == 1: # Missing the case where we hit a prime number but can then keep on going
            ptr = idx
            ones_in_path = 1
            found_non_one = False
            while ptr+e < len(nums) and (nums[ptr+e] == 1 or nums[ptr+e] in primes):
                if nums[ptr+e] in primes:
                    if found_non_one:
                        break
                    found_non_one = True
                else:
                    if found_non_one:
                        ones_in_path += 1
                ptr += e 
            result += ones_in_path if found_non_one else 0
    print(result)