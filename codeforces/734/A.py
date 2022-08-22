import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    if math.floor(n/3)*2 + math.ceil(n/3) == n:
        print(math.ceil(n/3), math.floor(n/3))
    else:
        print(math.floor(n/3), math.ceil(n/3))

