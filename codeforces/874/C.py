import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    a = list(map(int, line.split(" ")))
    if all(x % 2 == a[0] % 2 for x in a):
        print("YES")
        continue
    smallestodd = min(x for x in a if x % 2 == 1)
    for x in a:
        if x % 2 == 0:
            if x < smallestodd:
                print("NO")
                break
    else:
        print("YES")