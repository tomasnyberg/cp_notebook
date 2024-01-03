import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    n, k = map(int, line.split())
    for i in range(1, k+1):
        print(i, end=' ')
    for i in range(n, k, -1):
        print(i, end=' ')
    print()
