import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, B, x, y = list(map(int, line.split()))
    prev = 0
    result = 0
    for i in range(n):
        if prev + x <= B:
            result += prev + x
            prev = prev + x
        else:
            result += prev - y
            prev = prev - y
    print(result)