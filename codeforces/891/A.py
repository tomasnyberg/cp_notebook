import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    xs = list(map(int, line.split()))
    total = sum(xs)
    if total % 2 == 1:
        print("NO")
    else:
        print("YES")