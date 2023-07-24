import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, m, k, H = map(int, lines[ii].split())
    a = list(map(int, lines[ii+1].split()))
    result = 0
    for p in a:
        small, big = min(p, H), max(p, H)
        for i in range(1, m):
            if i*k + small == big:
                result += 1
                break
    print(result)