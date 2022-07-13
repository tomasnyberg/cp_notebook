import sys
lines = list(map(str.strip, sys.stdin.readlines()))
i = 1
while i < len(lines):
    a = list(map(int, lines[i+1].split(" ")))
    b = list(map(int, lines[i+2].split(" ")))
    biggest_diff = 0
    impossible = False
    for x, y in zip(a,b):
        diff = x - y
        biggest_diff = max(diff, biggest_diff)
    for j in range(len(a)):
        a[j] -= biggest_diff
        if a[j] < 0: a[j] = 0
    if a == b:
        print("YES")
    else:
        print("NO")
    i+=3
