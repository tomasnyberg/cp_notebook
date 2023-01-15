import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    left = 1
    right = n
    result = []
    while left < right:
        result.append(left)
        left += 1
        result.append(right)
        right -= 1
    if n % 2 == 1:
        result.append(left)
    print(*result)

