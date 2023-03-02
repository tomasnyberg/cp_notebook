import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    n, k = map(int, lines[i].split())
    a = list(lines[i+1])
    b = list(lines[i+2])
    if a == b:
        print("YES")
        continue
    if (list(sorted(a)) != list(sorted(b))):
        print("NO")
        continue
    for j in range(len(a)):
        if j - k < 0 and j + k >= len(a) and a[j] != b[j]:
            print("NO")
            break
    else:
        print("YES")
    