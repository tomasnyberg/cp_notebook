import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, a, b = map(int, line.split(" "))
    if b == 1:
        print("YES")
        continue
    if a == 1:
        print("YES" if (n-1) % b == 0 else "NO")
        continue
    i = 1
    while i <= n:
        if i % b == n % b:
            print("YES")
            break
        i *= a
    else:
        print("NO")

