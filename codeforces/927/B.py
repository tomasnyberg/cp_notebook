import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    xs = list(map(int, line.split()))
    curr = 0
    for x in xs:
        to_wait = x - curr % x
        curr += to_wait
    print(curr)