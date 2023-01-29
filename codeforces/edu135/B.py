import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    if n == 4:
        print(2,1,3,4)
        continue
    to_take = set(range(1, n+1))
    for x in [n, n-1, 1, 2, 3]:
        if x in to_take:
            to_take.remove(x)
    result = []
    for x in to_take:
        result.append(x)
    result += [2,3,1,n-1,n]
    print(*result)
