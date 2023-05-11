import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n = int(lines[i])
    i += 1
    xs = []
    ys = []
    for _ in range(n):
        x, y = map(int, lines[i].split(" "))
        xs.append(x)
        ys.append(y)
        i+=1
    xs.sort()
    ys.sort()
    a = 1
    if n % 2 == 0:
        a = xs[n//2]- xs[n//2-1] + 1
    b = 1
    if n % 2 == 0:
        b = ys[n//2]- ys[n//2-1] + 1
    print(a*b)