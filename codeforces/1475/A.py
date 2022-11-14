import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    good = False
    while n != 1:
        if n % 2 == 1:
            good = True
            break
        n //= 2
    print("YES" if good else "NO")
        