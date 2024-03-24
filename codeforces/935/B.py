import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    a, b, m = map(int, line.split())
    a, b = min(a, b), max(a, b)
    print(m // a + m//b + 2)