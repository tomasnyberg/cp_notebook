import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

coprimes = {} # i: set() for every num
for i in range(1, 1001):
    coprimes[i] = set()
    for j in range(1, 1001):
        if math.gcd(i, j) == 1:
            coprimes[i].add(j)


for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    available = set(nums)
    max_index = {}
    result = -1
    for idx, num in enumerate(nums):
        max_index[num] = idx + 1
    for num in available:
        for cp in coprimes[num]:
            if cp in available:
               result = max(result, max_index[num] + max_index[cp])
        
    print(result)
