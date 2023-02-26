import sys
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))

@lru_cache(None)
def recur(num):
    smallest = 32768 - num % 32768
    result = 0
    while num & ((1 << 15) - 1):
        num <<= 1
        result += 1
        smallest = min(smallest, result + (32768) - num % (32768))
    return min(smallest, result)

nums = list(map(int, lines[1].split()))
result = 0
for x in nums:
    smallest = 10**9
    for i in range(20):
        smallest = min(smallest, i + recur(x + i))
    print(smallest, end=' ')
print()