import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    a, b, c = map(int, line.split(" "))
    timeforfirst = abs(a - 1)
    timeforsecond = abs(b-c) + abs(c-1)
    if timeforfirst < timeforsecond:
        print(1)
    elif timeforfirst > timeforsecond:
        print(2)
    else:
        print(3)