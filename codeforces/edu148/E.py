import sys
lines = list(map(str.strip, sys.stdin.readlines()))

n, a1, x, y, m, k = map(int, lines[0].split(" "))

factorials = [1]
for i in range(1, n+1):
    factorials.append((factorials[-1]*i) % 998244353)

def nCr(n,r):
    if r > n: return 0
    import math
    return factorials[n] // (factorials[r]*(factorials[n-r]))

a = [a1]
for i in range(1, n):
    a.append((a[i-1] * x + y) % m)

b = []
for i, x in enumerate(a):
    total = 0
    for j in range(i+1):
        total += nCr((i+1) - j, k) * a[j]
    b.append(total)
        


result = 0
for i in range(len(b)):
    result ^= (i+1) * b[i]

print(a)
print(b)
print(result)