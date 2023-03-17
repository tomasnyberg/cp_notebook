import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    a, b = map(int, line.split())
    if a == 0 and b == 0:
        print(0)
    elif int(math.sqrt(a**2 + b**2))**2 == a**2 + b**2:
        print(1)
    else:
        print(2)