import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    n, t = map(int, lines[i].split())
    a = list(map(int, lines[i+1].split()))
    b = list(map(int, lines[i+2].split()))
    best = (-1, -1)
    for j in range(len(a)):
        if a[j] <= t:
            if b[j] >= best[1]:
                best = (j, b[j])
        t -= 1
    print(best[0] + 1 if best[0] != -1 else -1)