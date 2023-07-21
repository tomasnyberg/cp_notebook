import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))

def nPr(n, r):
    return math.factorial(n) // math.factorial(n-r)

def nCr(n,r):
    return math.factorial(n) // (math.factorial(r)*(math.factorial(n-r)))

def is_slope_1(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2 - x1 == 0:  # Avoid division by zero
        return False
    slope = (y2 - y1) / (x2 - x1)
    return slope == 1

def is_slope_minus1(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2 - x1 == 0:  # Avoid division by zero
        return False
    slope = (y2 - y1) / (x2 - x1)
    return slope == -1

ii = 1
while ii < len(lines):
    points = []
    n = int(lines[ii])
    ii+=1
    x_coords = {}
    y_coords = {}
    for _ in range(n):
        x, y = map(int, lines[ii].split())
        points.append((x,y))
        x_coords[x] = x_coords.get(x, 0) + 1
        y_coords[y] = y_coords.get(y, 0) + 1
        ii+=1
    result = 0
    for d in [x_coords, y_coords]:
        for val in d.values():
            if val < 2:
                continue
            result += nCr(val, 2)
    points.sort(key=lambda x: x[1])
    i = 0
    while i < len(points):
        j = i + 1
        while j < len(points):
            # Check if the slope between points[i] and points[j] is 1
            if not is_slope_1(points[i], points[j]):
                break
            j+=1
        if j - i >= 2:
            result += nCr(j-i, 2)
        i = j
    points.sort(key=lambda x: -x[1])
    i = 0
    while i < len(points):
        j = i + 1
        while j < len(points):
            # Check if the slope between points[i] and points[j] is 1
            if not is_slope_minus1(points[i], points[j]):
                break
            j+=1
        if j - i >= 2:
            result += nCr(j-i, 2)
        i = j
    print(result * 2)
