import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    l1, r1, l2, r2 = map(int, line.split())
    smallest_in_interval = None
    for i in range(l1, r1+1):
        if l2 <= i <= r2:
            smallest_in_interval = i
            break
    if smallest_in_interval is not None:
        print(smallest_in_interval)
    else:
        print(l1 + l2)
            