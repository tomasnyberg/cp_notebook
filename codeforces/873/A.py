import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    xs = []
    for i in range(1, n+1):
        xs.append(i if n % 2 == 1 else i*2)
    # assert sum(xs) % n == 0
    print(*xs)
