import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    a = list(map(int, lines[i+1].split()))
    b = list(map(int, lines[i+2].split()))
    res = 0
    for j in range(1, len(a)):
        res += min(abs(a[j] - a[j-1]) + abs(b[j] - b[j-1]), abs(a[j] - b[j-1]) + abs(b[j] - a[j-1]))
    print(res)