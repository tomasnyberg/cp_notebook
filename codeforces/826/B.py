import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    if n == 3 or n == 1:
        print(-1)
        continue
    if n == 2:
        print(2, 1)
        continue
    result = [0]*n
    for i in range(2, n):
        result[i] = i - 1
    result[1] = n
    result[0] = n-1
    print(*result) 