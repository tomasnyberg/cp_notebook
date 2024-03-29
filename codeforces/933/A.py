import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 3):
    n, m, k = map(int, lines[ii].split())
    a = list(map(int, lines[ii + 1].split()))
    b = list(map(int, lines[ii + 2].split()))
    result = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] + b[j] <= k:
                result += 1
    print(result)