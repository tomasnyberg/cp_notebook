import sys
from collections import deque
lines = list(map(str.strip, sys.stdin.readlines()))

n = int(lines[0])
s = lines[1]

ones = sum(1 for c in s if c == '1')
zeroes = sum(1 for c in s if c == '0')
a = 2**ones
b = 2**zeroes
for i in range(1, 2**n + 1):
    # print(i - a, 2**n - i - 1, "for number", i)
    if i - a >= 0 and 2**n - b - i + 1 >= 0:
        print(i, end=" ")
print()
