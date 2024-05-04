import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    n, a, b = map(int, line.split())
    if b / 2 < a:
        print(n//2*b + n%2*a)
    else:
        print(n*a)