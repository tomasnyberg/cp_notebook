import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    s = line
    a = 0
    b = 0
    seen_ratios = {}
    for c in s:
        if c == 'D':
            a += 1
        else:
            b += 1
        ratio = a / b if b != 0 else 10**10
        seen_ratios[ratio] = seen_ratios.get(ratio, 0) + 1
        print(seen_ratios[ratio], end=" ")
    print()
        