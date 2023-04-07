import sys
lines = list(map(str.strip, sys.stdin.readlines()))

n, s = int(lines[0]), lines[1]

a = 2**sum(1 for c in s if c == '1')
b = 2**sum(1 for c in s if c == '0')
for i in range(1, 2**n + 1):
    if i - a >= 0 and 2**n - b - i + 1 >= 0:
        print(i, end=" ")
print()
