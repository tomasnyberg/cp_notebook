import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    a = sum(map(int, line[:3]))
    b = sum(map(int, line[3:]))
    if a == b:
        print("YES")
    else:
        print("NO")