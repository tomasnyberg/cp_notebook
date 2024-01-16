import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 4):
    points = []
    for j in range(ii, ii+4):
        points.append(list(map(int, lines[j].split())))
    a = points[0]
    sides = []
    for point in points[1:]:
        if point[0] != a[0] and point[1] != a[1]:
            continue
        sides.append(abs(point[0]-a[0]) + abs(point[1]-a[1]))
    print(sides[0] * sides[1])