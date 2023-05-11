import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def mh(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def total_dist(p, points):
    return sum([mh(p, x) for x in points])

def find_minimum(points, idx, lr):
    left, right = 0, max([x[idx] for x in points])
    while left < right:
        mid = (left + right) // 2
        point = (0, mid) if idx else (mid, 0)
        pointb = (0, mid + 1) if idx else (mid + 1, 0)
        a, b = total_dist(point, points), total_dist(pointb, points)
        # If the middle element is greater than the next one, 
        # the minimum must be in the right part
        pred = a > b if lr else a >= b
        if pred:
            left = mid + 1
        # Otherwise the minimum is in the left part
        else:
            right = mid
    return left

i = 1
while i < len(lines):
    n = int(lines[i])
    points = []
    i+=1
    while n > 0:
        points.append(tuple(map(int, lines[i].split(" "))))
        i+=1
        n-=1
    l1, r1 = find_minimum(points, 0, True), find_minimum(points, 0, False)
    l2, r2 = find_minimum(points, 1, True), find_minimum(points, 1, False)
    print((r1 - l1 + 1) * (r2 - l2 + 1))