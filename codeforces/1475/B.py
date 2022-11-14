import sys
lines = list(map(str.strip, sys.stdin.readlines()))

possible = set()
for i in range(1000):
    for j in range(1000):
        if i*2020 + j*2021 > 2020*2021 - 2020-2021:
            break
        possible.add(i*2020 + j*2021)
for line in lines[1:]:
    n = int(line)
    if n >= 2020*2021 - 2020-2021 or n in possible:
        print("YES")
    else:
        print("NO")