import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 3):
    n, k = map(int, lines[ii].split())
    a = list(map(int, lines[ii+1].split()))
    b = list(map(int, lines[ii+2].split()))
    zipped = list(zip(a, b))
    biggest = 0
    total = 0
    result = 0
    for i, (x, y) in enumerate(zipped):
        total += x
        remaining = k - i - 1
        if remaining < 0:
            break
        biggest = max(biggest, y)
        result = max(result, total + biggest * remaining)
    print(result)

        
        