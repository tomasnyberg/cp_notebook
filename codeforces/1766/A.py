import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for x in lines[1:]:
    x = int(x)
    count = 0
    while x > 10:
        count += 9
        x //= 10
    count += x
    print(count)
        