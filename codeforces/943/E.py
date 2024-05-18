import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    n = int(line)
    if n == 2:
        print(1, 1)
        print(1, 2)
        continue
    if n == 3:
        print("""2 1
2 3
3 1""")
        continue
    points = [[1,1], [1,2]]
    for i in range(n, 2, -1):
        points.append([i, i])
    for x in points:
        print(*x)
