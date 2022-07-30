import sys
lines = list(map(str.strip, sys.stdin.readlines()))

n, q = map(int, lines[0].split(" "))

rowsattacked = {} # Which row is attacked : set of cols 
colsattacked = {} 
for i in range(1, len(lines)):
    query = list(map(int, lines[i].split(" ")))
    # print(rowsattacked)
    # print(colsattacked)
    # print()
    if query[0] == 1 or query[0] == 2:
        x, y = query[1:]
        if query[0] == 1:
            if y not in colsattacked: colsattacked[y] = set()
            colsattacked[y].add(x)
            if x not in rowsattacked: rowsattacked[x] = set()
            rowsattacked[x].add(y)
        else:
            colsattacked[y].remove(x)
            if len(colsattacked[y]) == 0: del colsattacked[y]
            rowsattacked[x].remove(y)
            if len(rowsattacked[x]) == 0: del rowsattacked[x]
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