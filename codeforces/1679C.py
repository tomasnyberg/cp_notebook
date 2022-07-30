from ftplib import all_errors
import sys
lines = list(map(str.strip, sys.stdin.readlines()))

n, q = map(int, lines[0].split(" "))

colsattacked = set()
rowsattacked = set()
for i in range(1, len(lines)):
    query = list(map(int, lines[i].split(" ")))
    print(rowsattacked)
    print(colsattacked)
    print()
    if query[0] == 1 or query[0] == 2:
        x, y = query[1:]
        if query[0] == 1:
            colsattacked.add(y)
            rowsattacked.add(x)
        else:
            colsattacked.remove(y)
            rowsattacked.remove(x)
        continue
    bad = False
    x1, y1, x2, y2 = query[1:]
    # print(x1, x2, y1, y2)
    all_good = True
    for x in range(x1, x2 + 1):
        if x not in rowsattacked:
            all_good = False
            break
    if all_good:
        print("YES")
        continue
    all_good = True
    for y in range(y1, y2+1):
        if y not in colsattacked:
            all_good = False
            break
    print("YES" if all_good else "NO")