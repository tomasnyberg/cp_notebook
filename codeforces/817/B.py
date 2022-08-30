import sys
lines = list(map(str.strip, sys.stdin.readlines()))

same = set(['G', 'B'])

for i in range(1, len(lines), 3):
    a = lines[i+1]
    b = lines[i+2]
    bad = False
    for j in range(len(a)):
        if (a[j] == 'R' and b[j] in same) or (b[j] == 'R' and a[j] in same):
            bad = True
            break
    print("YES" if not bad else "NO")