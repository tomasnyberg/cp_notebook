import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    n, k = map(int, lines[i].split())
    a = lines[i+1]
    b = lines[i+2]
    if (list(sorted(a)) != list(sorted(b))):
        print("NO")
        continue
    a = list(a)
    b = list(b)
    if len(a) == 3 and a != b:
        print("NO")
        continue
    if len(a) == 4 and a != b:
        if a[0] == b[-1] and a[-1] == b[0] and a[1] == b[1] and a[2] == b[2]:
            print("YES")
            continue
        else:
            print("NO")
            continue
    if len(a) == 5 and a[2] != b[2]:
        print("NO")
        continue
    print("YES")