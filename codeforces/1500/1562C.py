import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import math
import random

# for j in range(1, 25, 2):
#     onlyones = (1 << j) - 1
#     for i in range(2, int(math.sqrt(onlyones)) + 5):
#         if onlyones % i == 0 and all([c == '1' for c in bin(i)[2:]]):
#             if len(bin(onlyones)[2:]) // 2 > len(bin(i)[2:]): continue
#             print(onlyones, i, bin(i), len(bin(i)[2:]))


def find(s):
    zero = -1
    if all(c == '1' for c in s):
        return (1, len(s) - 1, 2, len(s))
    for i in range(len(s)):
        if s[i] == '0':
            zero = i
    if len(s) % 2 == 1 and zero == len(s) // 2:
        return (len(s) // 2 + 1, len(s), len(s) // 2 + 2, len(s))
    if zero < len(s) // 2:
        return (zero + 1, len(s), zero + 2, len(s))
    else:
        return(1, zero + 1, 1, zero)

for i in range(100000):
    num = random.randint(1, 100000)
    s = bin(num)[2:]
    if all(c == '1' for c in s) and len(s) % 2 == 1:
        continue
    a, b, c, d = find(s)
    if a == 0 or c == 0 or d == 0 or b == 0:
        print(s, a, b, c, d)
        print(int(s[a-1:b], 2), int(s[c-1:d], 2))
        print()
    if int(s[a-1:b], 2) == 0 or int(s[c-1:d], 2) == 0: continue
    if int(s[a-1:b], 2) % int(s[c-1:d], 2) != 0:
        print(s, a, b, c, d)
        print(int(s[a-1:b], 2), int(s[c-1:d], 2))
        print()
    if b - a + 1 < len(s) // 2 or d - c + 1 < len(s) // 2:
        print(s, a, b, c, d)
        print(int(s[a-1:b], 2), int(s[c-1:d], 2))
        print()
    if a == c and b == d:
        print(s, a, b, c, d)
        print(int(s[a-1:b], 2), int(s[c-1:d], 2))
        print()

for line in lines[2::2]:
    s = line
    print(*find(s))