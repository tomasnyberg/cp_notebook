import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, k = map(int, line.split())
    if n == 1 and k != 1:
        print("NO")
        continue
    if n % 2 == 0:
        print("YES")
        continue
    if k == 1 or k == n:
        print("YES")
        continue
    if (n % k) % 2 == 0:
        print("YES")
        continue
    if k > n:
        print("NO")
        continue
    if n - k > 1 and (n - k) % 2 == 0:
        print("YES")
        continue
    print("NO")