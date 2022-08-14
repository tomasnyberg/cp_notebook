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
    for idx, num in enumerate(nums):
        if num in primes:
            ptr = idx
            ones_in_path = 0
            while ptr+e < len(nums) and nums[ptr+e] == 1:
                ones_in_path +=1
                ptr += e 
            result += ones_in_path
        if num == 1:
            ptr = idx
            ones_in_path = 1
            found_non_one = False
            while ptr+e < len(nums) and (nums[ptr+e] == 1 or nums[ptr+e] in primes):
                if nums[ptr+e] in primes:
                    result += ones_in_path
                    found_non_one = True
                    break
                else:
                    ones_in_path += 1
                ptr += e 
    print(result)
    # # print(nums)
    # # print(prim)
    # print()