import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    a, b = map(int, line.split())
    result = b - a
    for i in range(b-a+1):
        new_a = (a + i)|b
        result = min(result, i + 1 + (new_a - b))
    for i in range(b-a+1):
        new_b = b + i
        new_a = a | new_b
        if new_b == new_a:
            result = min(result, i + 1)
    print(result)


