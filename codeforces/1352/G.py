import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    if n < 4:
        print(-1)
        continue
    result = []
    for i in range(n, 0, -1):
        if i % 2 == 1:
            result.append(i)
    result.append(4)
    result.append(2)
    for i in range(6, n+1):
        if i % 2 == 0:
            result.append(i)
    for x in result:
        print(x, end=" ")
    print()

